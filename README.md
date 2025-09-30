###  Data Processing Project
This project shows how to clean, transform, engineer features, and aggregate transaction data.  
It is intended to assist in learning data wrangling, feature engineering, and basic analytics with pandas and Python classes.

### Quick start/ Setting up environment
1. Create a virtual environment
    python -m venv venv
2. Activating Virtual environment\
    ./venv/Scripts/Activate
3. Installing dependencies
    pip install ./utilities/requirements.txt

### Key Features
**Bulk loading data in a dictionary** - Bulk loading the merged dataframe into a dictionary using Transaction Class.
**Quick Profiling** - quickly analysing the data, getting the min,max,mean of prices and checking the unique cities.
**Spotting the Grime(dirty data cases)** identigying at least 3 dirty data cases
**Clean the data - def clean()** - cleaning the missing city names and coupon codes and normalizes the city formats
**Transform the Data - def transform()** - modifies coupon codes into percentage discounts
**Feature Engineering - def engineer-features()** - adds new column called days_since_ purchased.
**Minimum Aggregation** - Calculating Revenue per city
**Saving cleaned data into a JSON file - def to_dict()** - converting to a JSON compatible dictionary

### Data Sources
1000SalesRecord.csv - https://excelbianalytics.com/wp/wp-content/uploads/2017/07/1000-Sales-Records.zip
synthetic_data.csv - synthetically generated. Code used is in ./syntheticdatagenerate.py


