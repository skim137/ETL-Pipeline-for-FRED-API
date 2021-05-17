# ETL-Pipeline-for-FRED-API
Create an ETL pipeline for FRED® API (St. Louis Fed Web services) using Python and SQLite.

## Background
The St. Louis Fed's FRED (Federal Reserve Economic Data) provides US and international economic and financial time series data via its website, an Excel add-in tool, and a Web service. There are many third party applications (API wrappers) that are written in multiple programming languages including Python (you can find them [here](https://fred.stlouisfed.org/docs/api/fred/)) to access the data through the Web service.    

This ETL pipeline project contains a Python script that creates/updates an SQLite database file which will interact with FRED API to retrieve data based on five key API parameters users can set for each data series. This solution allows users to store data from FRED API on a persistent manner and also minimizes the number of API requests they have to make every time they need data. Since retrieved data are stored in a tabular SQL table, they can transform them whichever they want and do further analysis using data analysis tools such as pandas and R.

Using SQLiteStudio is highly recommended. This excellent open source interface program can be [downloaded here](https://sqlitestudio.pl/). For those who want to use the SQLite command line tools, download them from [here](https://www.sqlite.org/download.html). Users are also expected to have some familiarity with the [sqlite3 module](https://docs.python.org/3/library/sqlite3.html#), but this is not required.

Lastly, users are expected that they have used FRED data before and understand different ways of querying FRED data.

## Instructions
1. Obtain a 32 character lower-cased alpha-numeric API key. You can get one [here](https://research.stlouisfed.org/useraccount/login/secure/).
2. Insert your API key in line 13 of *fredapi_etl.py*.
3. Execute *fredapi_etl.py* in the terminal or an IDE. 
4. Check the folder where *fredapi_etl.py* is saved to make sure an SQLite db file called *fredapi* is created.
5. Set API parameters in *parameters* table (more on this below). As an example, you may run *INSERT INTO parameters.sql*, which includes 8 data series from FRED's homepage.
6. Execute *fredapi_etl.py* in the terminal or an IDE again. If successful, *freddata* table should have data loaded.

## API Parameters
