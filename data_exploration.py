# Pandas and matplotlib libraries will be used for data exploration.
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # The data set contains information about public transport journeys by type of transport.
    # The prepared CSV file (from data_preparation.py) with the data will be used.

    # Reading CSV file with the prepared data set and storing it in the dataframe.
    df = pd.read_csv('prepared_dataset.csv')

    # According to TfL, Emirates Airline did not run during Period 1.
    # Moreover, it is not essential public transportation type. Hence, it can be removed for the data exploration part.
    df = df.drop(['Emirates Airline Journeys (m)'], axis=1)

    # The numbers for Overground journey are only reliable from October 2010.
    # The prepared data set is from the period of January 2018 to the August 2021. Therefore, it is not a problem.
    ax = plt.gca()
    plt.plot(df['Period ending'], df['Bus journeys (m)'], label="Bus journeys")
    plt.plot(df['Period ending'], df['Underground journeys (m)'], label="Underground journeys")
    plt.plot(df['Period ending'], df['DLR Journeys (m)'], label="DLR journeys")
    plt.plot(df['Period ending'], df['Tram Journeys (m)'], label="Tram journeys")
    plt.plot(df['Period ending'], df['Overground Journeys (m)'], label="Overground journeys")
    plt.plot(df['Period ending'], df['TfL Rail Journeys (m)'], label="Rail journeys")
    plt.legend()
    plt.title('Usage of public transport by journey types in London')
    plt.xlabel('Period ending (date)')
    plt.ylabel('Journeys (millions)')
    plt.xticks(rotation=90)
    plt.show()
    plt.savefig('usage_by_journey_types')

    boxplot = df.boxplot(column=['Bus journeys (m)'])
    boxplot.plot()
    plt.show()
    plt.savefig('boxplot_bus_journeys')

    # Questions:
    # - Is there any pattern in the changes of usage for public transportation in London?
    # - Which group of public transportation consumers use the most?
    # - Which category of people usually uses transport at that time?
    # - Are trends similar to the performance before the pandemic?
    # - Is it possible to reduce the overcrowding on certain types of transport?

    # Period lengths (in days) are different in periods 1 and 13.

    # DLR journeys are based on automatic passenger counts at stations.
    # Overground and Tram journeys are based on automatic  on-carriage passenger counts.
    # This data excludes retrospective revisions to bus journeys
    # The journey figures for Period 1 are estimates and are subject to retrospective adjustment

