**longevity_factors_by_country**
This package provides data on various factors that surround and potentially influence longevity by country. Data includes the average lifespan, healthcare expenditure, by country, education spend, and more.

**Installation**
$ pip install longevity_factors_by_country
Purpose:
The purpose of this package is understand macro trends that can impact life expectancy at a national level over the span of several years. I've included data about health spend as a percentage of GDP, education spend as a percentage of GDP, happiness levels, inequality presented with the Gini coefficient.

I chose the data project option for my project.
Here is the package: https://pypi.org/project/longevity_factors_by_country/ Install the package: pip install longevity_factors_by_country

**Install tests**
pip install -i https://test.pypi.org/simple/ longevity_factors_by_country

**Important Information**
Data is uploaded in the "DataForPackage" Folder I used Amazon RDS to store my data using postgresql. You can access the database by the following credentials: Login: qmssanj - username qmssproject2023 - password

Command to access the database: psql --host=database-qmss-anj.c8fpusvnobjg.us-east-2.rds.amazonaws.com --port=5432 --username=qmssanj password --dbname=postgres`

**Code**
In the DataDisplay.ipynb in the Final Project folder, I display the data that I've collected, cleaned, and aggregated. I also display two functions that I made to show highest and lowest values. clean_data.py has most of the substance of my project, that's where I do all of the data wrangling. Usage longevity_factors_by_country.py contains all methods that are meant to be used publicly

getLongevityDataForYear is the primary method for data display, start here when you import the package. This method takes a year in string format and returns all countries and their relevant columns for that year.

Once you have a data frame from this function, you can use other methods.

getCountriesWithTopLifeSpan takes the data frame and an integer, n, it then returns the n countries with the longest life spans for the data frame

getCountriesWithLowestLifeSpan takes the data frame and an integer, n, it then returns the n countries with the lowest life spans for the data frame

**Contributing**
Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

**License**
longevity_factors_by_country was created by Anjana Rao. It is licensed under the terms of the MIT license.

**Credits**
longevity_factors_by_country was created with cookiecutter and the py-pkgs-cookiecutter template.
