# ETL-Pipeline-for-FRED-API
Create an ETL pipeline for FRED® API (St. Louis Fed Web services) using Python and SQLite.

## Background
The St. Louis Fed's FRED (Federal Reserve Economic Data) provides US and international economic and financial time series data via its website, an Excel add-in tool, and a Web service. There are many third party applications (API wrappers) that are written in multiple programming languages including Python (you can find them [here](https://fred.stlouisfed.org/docs/api/fred/)) to access the data through the Web service.    

This ETL pipeline project contains a Python script that creates/updates an SQLite database file which will interact with FRED API to retrieve data based on five key API parameters users can set for each data series. This solution allows users to store data from FRED API on a persistent manner and also minimizes the number of API requests they have to make every time they need data. Since retrieved data are stored in a tabular SQL table, they can transform them whichever they want and do further analysis using data analytics tools such as Pandas and R.

