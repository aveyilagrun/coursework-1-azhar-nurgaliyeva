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

    # Period lengths (in days) are different in periods 1 and 13.
    # This is why plots should be approached by using ending of reporting periods.
    # Plotting the graph of usage of different journey types in London.
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
    # There was a problem with saving matplotlib figures on my laptop, which is why I used screenshot in the README.md.
    # For some reason saved figure would appear blank in the folder.

    # Question 1: "Is there any pattern in the changes of usage for public transportation in London?"

    # Answer 1: "The usage of public transportation in London was more popular before the coronavirus pandemic in 2020.
    # There is a huge decrease in the utilisation of public transport during the period of March-May 2020. This was
    # caused by the national lockdown and extensive fear of coronavirus. A few months after that the indicators started
    # to improve, but in December-March 2021 there was another wave of coronavirus fear due to the emergence of Alpha
    # Covid variant. It was first identified in Kent, UK. Since that period, the usage of public transportation is
    # improving, but at a relatively slower rate."

    # Question 2: "Which group of public transportation consumers use the most?"

    # Answer 2: "The most popular and the most used type of transport is bus. Underground is in the second place in
    # terms of popularity. Buses probably win as there are more routes and bus stops across London than tube stations.
    # Moreover, the price for bus journey is much cheaper than for underground journey. Overground, DRL, rail and tram
    # journeys are significantly less popular than bus and underground. Their usage remains about the same level as
    # before the coronavirus pandemic."

    # Question 3: "Which category of people usually uses this type of transport the most?"

    # Answer 3: "Buses and underground are mostly used by the people who are either working full-time or studying in
    # university. Therefore, the profile of a person who uses these 2 types of public transport the most are people
    # in their 20-30s who need to commute every day."

    # Plotting the boxplot in order to check for outliers in the data for bus journeys.
    boxplot = df.boxplot(column=['Bus journeys (m)'])
    boxplot.plot()
    plt.show()
    plt.savefig('boxplot_bus_journeys')
    # There was a problem with saving matplotlib figures on my laptop, which is why I used screenshot in the README.md.
    # For some reason saved figure would appear blank in the folder.

    # Question 4: "Are trends similar to the performance before the pandemic?"

    # Answer 4: "The amount of journeys is still smaller than before the pandemic, but in recent months the number of
    # journeys is steadily increasing. The minimum indicator of the data for bus journey is around 30 millions, whereas
    # maximum is approximately 185 millions. The average value is around 155 millions bus journeys. There are no
    # significant outliers in the data, if you do not consider national lockdown period as the outlier. All of these
    # characteristics would probably be higher if coronavirus pandemic did not happen. It will take some time for
    # the transport sector to fully recover the amount of public transport journeys."

    # Question 5: "Is it possible to reduce the overcrowding on certain types of transport?"

    # Answer 5: "There is a possibility of reducing the pressure on bus journey as they are still heavily overcrowded,
    # compared to all the other types of transport. In order to do that the strategy of reducing prices or introducing
    # certain discount on other journey types should be considered. Underground, overground, DLR and rail journeys
    # usually cost more than bus journey, which is why people might prefer that over anything else."

    # Important notes:
    # - DLR journeys are based on automatic passenger counts at the stations, whereas overground and tram journeys
    # count passengers automatically on-carriage.
    # - The numbers for reporting period 1 are approximations which were deduced using retrospective adjustment.
    # - This data set did not include any alterations to the bus journeys numbers due to adjustments.
