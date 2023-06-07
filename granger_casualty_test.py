import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests
import sys
import io


def perform_granger_test(df1, df2, maxlag, test='ssr_chi2test'):
    # Ensure that the dataframes are sorted by index (assumed to be the time variable)
    df1 = df1.sort_index()
    df2 = df2.sort_index()

    # Initialize an empty dictionary to store the results
    results = {}

    # Perform the Granger Causality test for each column in df2
    for column in df2.columns:
        data = pd.concat([df1['Market Cap(0.1billion CNY)'], df2[column]], axis=1)

        # Temporarily redirect console output to a string
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()

        result = grangercausalitytests(data, maxlag)

        # Restore console output
        sys.stdout = old_stdout

        # Extract the test results from the console output
        output = mystdout.getvalue()

        p_values = [round(result[i+1][0][test][1],4) for i in range(maxlag)]
        min_p_value = min(p_values)
        results[column] = min_p_value

        # Save the console output to a text file
        with open(f'results/{column}_granger_results.txt', 'w') as f:
            f.write(output)

    # Save the minimum p-values to a CSV file
    pd.DataFrame(results, index=['Min p-value']).transpose().to_csv('results/granger_test_results.csv')

    print('Granger Causality Test results saved to granger_test_results.csv')

    return pd.DataFrame(results, index=['Min p-value']).transpose()
