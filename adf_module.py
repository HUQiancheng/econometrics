import pandas as pd
from statsmodels.tsa.stattools import adfuller


def perform_adf_test(file_name):
    # Set the number of columns to display
    pd.set_option("display.max_columns", None)

    # Read the CSV file into a DataFrame
    data = pd.read_csv(file_name)

    # Select the relevant columns
    columns = data.columns[1:]

    # Initialize an empty DataFrame to store the results
    results_df = pd.DataFrame(columns=['Series', 'ADF Statistic', 'p-value', '1%', '5%', '10%'])

    # Perform the ADF test for each series
    for column in columns:
        series = pd.to_numeric(data[column], errors='coerce')
        result = adfuller(series.dropna())
        temp_df = pd.DataFrame([{
            'Series': column,
            'ADF Statistic': result[0],
            'p-value': result[1],
            '1%': result[4]['1%'],
            '5%': result[4]['5%'],
            '10%': result[4]['10%']
        }])
        results_df = pd.concat([results_df, temp_df], ignore_index=True)

    return results_df
