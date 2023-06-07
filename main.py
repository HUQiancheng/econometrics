import tkinter as tk
from tkinter import filedialog
import os
from adf_module import perform_adf_test


def main():
    # Initialize tkinter - we won't be using the root window but we need it to create the file dialog
    root = tk.Tk()
    # Hide the main window because we only want to show the file dialog
    root.withdraw()

    # Open a file dialog and get the selected file's path
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

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


if __name__ == "__main__":
    main()
