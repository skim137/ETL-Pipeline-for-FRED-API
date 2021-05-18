# ETL-Pipeline-for-FRED-API
Create an ETL pipeline for FRED® API (St. Louis Fed Web services) using Python and SQLite.

## Background
The St. Louis Fed's FRED (Federal Reserve Economic Data) provides US and international economic and financial time series data via its website, an Excel add-in tool, and a Web service. There are many third party applications (API wrappers) that are written in multiple programming languages including Python (you can find them [here](https://fred.stlouisfed.org/docs/api/fred/)) to access the data through the Web service.    

This ETL pipeline project contains a Python script that creates and updates an SQLite database file which will interact with the FRED API service to retrieve data incrementally based on five key API parameters users can set for each data series. This solution allows users to store data from FRED API on a persistent manner and also minimizes the number of API requests they have to make every time they need data. Since retrieved data are stored in a tabular SQL table, users can export them to pandas, R, and BI tools to perform further analysis.  

Using SQLiteStudio is highly recommended. This excellent open source interface program can be [downloaded here](https://sqlitestudio.pl/). For those who want to use the SQLite command line tools instead, download them from [here](https://www.sqlite.org/download.html). Users are expected to have some familiarity with the [sqlite3 module](https://docs.python.org/3/library/sqlite3.html#), but it is not required. Lastly, users are expected that they have used FRED data before and understand different ways of querying FRED data.

## Instructions
1. Obtain a 32 character lower-cased alpha-numeric API key. You can get one [here](https://research.stlouisfed.org/useraccount/login/secure/).
2. Assign your API key to a variable named *fredkey* in line 13 of *fredapi_etl.py*.
3. Execute *fredapi_etl.py* in the terminal or an IDE. 
4. Check the folder where *fredapi_etl.py* is saved to make sure an SQLite db file called *fredapi* is created.
5. Set API parameters in *parameters* table (more on this below). As an example, you may run *INSERT INTO parameters.sql*, which includes 8 data series from FRED's homepage.
6. Execute *fredapi_etl.py* in the terminal or an IDE again. If successful, *freddata* table should have data loaded.

## API Parameters
Setting correct API parameter values in *parameters* table is extremely important. You can refer to FRED's documentation [here](https://fred.stlouisfed.org/docs/api/fred/series_observations.html). There are 6 columns you can set:
* *series_desc*: create a unique name you can assign for the data series you are retrieving. This is the table's primary key and used for *ticker* column in *freddata* table.
* *series_id*: input FRED's series id for the data series you are retrieving. For example, the id for the US employment rate is *UNRATE*.
* *observation_start*: set a starting date ('YYYY-MM-DD') for the data series you are retrieving. Note that there is no functionality to set an observation end date in this tool.
* *units*: this defines the unit of your data series. You may insert *NULL* which will, by default, retrieve untransformed data.
* *frequency*: this defines the date frequency of your data series. Higher frequency data series can be converted to lower frequency (ex. daily rates to a monthly average). You may insert *NULL* which will, by default, retrieve untransformed data.
* *aggregation_method*: if *frequency* is something other than *NULL*, then you can define the aggregation method of your data series. You may insert *NULL* which will, by default, retrieve averaged data by period.

**units**
Parameter value | Description
------------ | -------------
NULL | default: lin (No transformation)
lin | Levels (No transformation)
chg | Change
ch1 | Change from Year Ago
pch | Percent Change
pc1 | Percent Change from Year Ago
pca | Compounded Annual Rate of Change
cch | Continuously Compounded Rate of Change
cca | Continuously Compounded Annual Rate of Change
log | Natural Log


**frequency**
Parameter value | Description
------------ | -------------
NULL | default frequency of the series
d | Daily
w | Weekly
bw | Biweekly
m | Monthly
q | Quarterly
sa | Semiannual
a | Annual


**aggregation_method**
Parameter value | Description
------------ | -------------
NULL | default: avg
avg | Average
sum | Sum
eop | End of Period


**parameter table example**

