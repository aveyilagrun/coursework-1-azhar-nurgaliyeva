# Pandas and matplotlib libraries will be used for data exploration.
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # The data set contains information about public transport journeys by type of transport.
    # The prepared CSV file (from data_preparation.py) with the data will be used.

    # Reading CSV file with the prepared data set and storing it in the dataframe.
    df = pd.read_csv('prepared_dataset.csv')



    print(df)