import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Set the number of columns to display
pd.set_option("display.max_columns", None)

# Read the CSV file into a DataFrame, skipping the header row
data = pd.read_csv("fc01cc01-9242-48c6-a082-729ff3de007a_Series - Metadata.csv", skiprows=1)

# Transpose the DataFrame
data = data.T

# Set the first row as column headers
data.columns = data.iloc[0]

# Remove the first row (header row)
data = data[1:]

# Perform the ADF test for each series
for column in data.columns:
    series = pd.to_numeric(data[column], errors='coerce')
    result = adfuller(series.dropna())
    print("Series:", column)
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
    print("Critical Values:")
    for key, value in result[4].items():
        print(f"\t{key}: {value}")
        print()
