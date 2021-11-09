# Pandas library will be used for data preparation.
import pandas as pd

if __name__ == '__main__':
    # The data set contains information about public transport journeys by type of transport.
    # Both Excel and CSV files of the data set are saved in the "data" folder.

    # Reading CSV file with the data set and storing it in the dataframe.
    df = pd.read_csv('data/tfl-journeys-type.csv')

    # Deleting all the rows with null (missing) values.
    df = df.dropna()

    # Remove a single column with the name 'Reporting Period'.
    df = df.drop(['Reporting Period'], axis=1)

    # Limit the data from 2018 to the present time
    df = df.iloc[-47:]

    # Reset the index to avoid the problems with it
    df = df.reset_index(drop=True)

    # Printing the prepped DataFrame
    print(df)

    # Save the dataframe to a new CSV file. Row names will not be saved.
    df.to_csv("prepared_dataset.csv", index=False)
