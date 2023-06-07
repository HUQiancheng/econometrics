import tkinter as tk
import pandas as pd
from tkinter import filedialog, simpledialog
import os
from adf_module import perform_adf_test
from granger_casualty_test import perform_granger_test


def main():
    # Initialize tkinter - we won't be using the root window but we need it to create the file dialog
    root = tk.Tk()
    # Hide the main window because we only want to show the file dialog
    root.withdraw()

    # Open a file dialog and get the selected file's path
    file_path = filedialog.askopenfilename(title="Provide raw data", filetypes=[("CSV files", "*.csv")])

    # Perform the ADF test and save the results
    results_df = perform_adf_test(file_path)

    # Get the file name without the directory
    file_name = os.path.basename(file_path)
    # Remove the extension
    base_name = file_name.rsplit('.', 1)[0]

    # Define output file name and add the "results" directory to the path
    output_file_path = "results/" + base_name + "_adf_test_results.csv"

    # Create the results directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # Save the DataFrame to a CSV file
    results_df.to_csv(output_file_path, index=False)

    print("ADF test results saved to", output_file_path)

    # Initialize tkinter - we won't be using the root window but we need it to create the file dialog
    root = tk.Tk()
    # Hide the main window because we only want to show the file dialog
    root.withdraw()

    # Open a file dialog and get the selected file's paths
    file_path1 = filedialog.askopenfilename(title="Provide BANK data", filetypes=[("CSV files", "*.csv")])
    file_path2 = filedialog.askopenfilename(title="Provide FDI data", filetypes=[("CSV files", "*.csv")])

    # Read the CSV files into DataFrames
    df1 = pd.read_csv(file_path1, index_col=0)
    df2 = pd.read_csv(file_path2, index_col=0)

    # Ask the user for the maximum lag
    maxlag = simpledialog.askinteger("Input", "Enter maximum lag", parent=root)

    # Perform the Granger Causality Test and get the results

    results_df_gct = perform_granger_test(df1, df2, maxlag)

    print("All granger results saved")


if __name__ == "__main__":
    main()
