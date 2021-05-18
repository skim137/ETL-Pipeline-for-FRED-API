## -----------------------------------------------------------
# Desc: Create an ETL pipeline for FRED API's market and economic time series data
# 
# Last updated: 2021-05-17
# Author: http://www.github.com/skim137
## -----------------------------------------------------------

import os
import requests
import sqlite3

#Assign your FRED API Key (as string) to the fredkey variable below. You can get one here - https://research.stlouisfed.org/useraccount/login/secure/
fredkey = ''

if len(fredkey) != 32:
    print('Please make sure to enter your FRED API key. See line 12.', '\n ')
    input('Hit enter to exit.')
    os._exit(1)
else:
    pass


#SQLite connection
dbname = 'fredapi2.sqlite3'
dbpath = os.path.join(os.path.dirname(__file__), dbname)

conn = sqlite3.connect(dbpath)
c = conn.cursor()


#SQL operations
create_parameters = '''CREATE TABLE IF NOT EXISTS parameters (series_desc TEXT NOT NULL, 
                    series_id TEXT NOT NULL, 
                    observation_start TEXT NOT NULL, 
                    units TEXT, 
                    frequency TEXT, 
                    aggregation_method TEXT, 
                    CONSTRAINT PK_parameters PRIMARY KEY (series_desc), 
                    CHECK (units IN('lin', 'chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log') OR units IS NULL), 
                    CHECK (frequency IN('d', 'w', 'bw', 'm', 'q', 'sa', 'a') OR frequency IS NULL), 
                    CHECK (aggregation_method IN('avg', 'sum', 'eop') OR aggregation_method IS NULL)
                    )
'''

create_freddata = '''CREATE TABLE IF NOT EXISTS freddata (date TEXT NOT NULL, 
                    ticker TEXT NOT NULL, 
                    value REAL NOT NULL, 
                    CONSTRAINT PK_freddata PRIMARY KEY (date, ticker), 
                    CONSTRAINT FK_freddata FOREIGN KEY (ticker) 
                    REFERENCES parameters(series_desc)
                    )
'''

insert_freddata = 'INSERT INTO freddata (date, ticker, value) VALUES (?, ?, ?)'

requests_control = '''SELECT series_desc, series_id, 
                    CASE
                        WHEN t.max_date IS NULL THEN observation_start
                        WHEN t.max_date >= observation_start THEN t.max_date
                        ELSE t.max_date
                    END start_date,
                    
                    CASE
                        WHEN t.max_date IS NULL THEN 'observation_start'
                        WHEN t.max_date >= observation_start THEN 'max_date'
                        ELSE 'max_date'
                    END insert_indicator,
                    
                    units, frequency, aggregation_method

                    FROM parameters

                    LEFT JOIN 
                        (SELECT ticker, MAX(date) AS max_date
                        FROM freddata
                        GROUP BY ticker) AS t

                    ON parameters.series_desc = t.ticker
'''

c.execute(create_parameters)
conn.commit()

c.execute(create_freddata)
conn.commit()


#Request data series from FRED API based on the requests_control query and insert the responses into freddata table
c.execute(requests_control)

result = c.fetchall()

for row in result:

    parameters = {  'api_key': fredkey,
                    'series_id': row[1],
                    'observation_start': row[2],
                    'units': row[4],
                    'frequency': row[5],
                    'aggregation_method': row[6],
                    'file_type': 'json'}
    
    try:
        response = requests.get('https://api.stlouisfed.org/fred/series/observations', params=parameters)
        response.raise_for_status()
        
    except requests.exceptions.HTTPError:
        print("An error occured for ticker, '" + row[0] + "' (series_id: " + row[1] + ').', 'See below for more details.', '\n ')
        print(response.json(), '\n ')
        
    except requests.exceptions.ConnectionError:
        print('A network problem occured.')
        break
        
    except requests.exceptions.Timeout:
        print('A request timeout occured.')
        break

    except requests.exceptions.RequestException as e:
        print('An unknown error occured.')
        break
        
    else:
        output = response.json()
        
        series = output['observations']
        
        records = [(i['date'], row[0], float(i['value'])) if i['value'] != '.' else None for i in series]

        records = list(filter(lambda x: x is not None, records))
        
        if row[3] == 'observation_start':
        
            c.executemany(insert_freddata, records)
            
        elif row[3] == 'max_date':
        
            records = records[1:]
            
            c.executemany(insert_freddata, records)
        
        conn.commit()

conn.close()