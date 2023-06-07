import pandas as pd
import numpy as np
import statsmodels.api as sm
from tkinter import Tk, Label, Button, Entry

class ARDLApp:
    def __init__(self, window):
        self.window = window
        window.title("ARDL Analysis")

        self.label = Label(window, text="Enter the ARDL order parameters (p, q):")
        self.label.pack()

        self.entry = Entry(window)
        self.entry.pack()

        self.analyze_button = Button(window, text="Analyze", command=self.analyze)
        self.analyze_button.pack()

        self.close_button = Button(window, text="Close", command=window.quit)
        self.close_button.pack()

    def analyze(self):
        p, q = map(int, self.entry.get().split(','))

        # Read data
        bank_data = pd.read_csv('data/bank_data.csv')
        fdi_data = pd.read_csv('data/fdi_data.csv')

        # Apply ARDL model
        for column in fdi_data.columns:
            y = bank_data['Market Cap(0.1billion CNY)']
            X = fdi_data[column]

            # Ensure that X and y have the same index
            common_index = y.index.intersection(X.index)
            y = y.loc[common_index]
            X = X.loc[common_index]

            # Add constant to exog
            X = sm.add_constant(X)

            # Fit the ARDL model
            model = sm.tsa.ARDL(y, lags=p, exog=X, order=q).fit()

            print(f"Results for column {column}:")
            print(model.summary())


root = Tk()
my_app = ARDLApp(root)
root.mainloop()
