import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    
    
    city_selection = input('To view the available bikeshare data, kindly type:\nThe letter (a) for Chicago\n\
The letter (b) for New York City\nThe letter (c) for Washington\n').lower()
     
    valid_input=["a", "b", "c"]
    
    while city_selection not in valid_input:
        city_selection=(input('Invalid Input, to view the available bikeshare data, kindly type:\nThe letter (a) for \
Chicago\nThe letter (b) for New York City\nThe letter (c) for Washington\n')).lower()
    
    if city_selection == "a":
        city="chicago"
    elif city_selection == "b":
        city= "new york city"
    elif city_selection == "c":
        city= "washington"
    # TO DO: get user input for month (all, january, february, ... , june)
    valid_filteration_variable=['Month', 'Day', 'None', 'Both']
    
    filter_variable =input('\n\nWould you like to filter {}\'s data by month, day, both, or not at all? type month or day or both or none: \n'.format(city.title())).title()
    
    while filter_variable not in valid_filteration_variable:
            filter_variable =input('\n\nInvalid Input, Would you like to filter {}\'s data by month, day, both, or not at all? type month or day or both or none: \n'.format(city.title())).title()
            
    months=['All','January','February','March','April','May','June']
    days=['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
###################################################################################
    if filter_variable=='Month':
        month=(input("kindly type the month from the available data below:\nJanuary, February, March, April, May, June or all\n")).title()
           
        while month not in months:
            month=(input("Invalid Input,kindly type the month from the available data below:\nJanuary, February, March, April, May, June or all\n")).title()
        day='All'
###################################################################################
    elif filter_variable == 'Day':
        day=(input("kindly type the day from the available data below:\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all \n")).title()

        while day not in days:
            day=(input("Invalid Input kindly type the day from the available data below:\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all\n")).title()
        month='All'
###################################################################################
    elif filter_variable == 'Both':
        month=(input("kindly type the month from the available data below:\nJanuary, February, March, April, May, June or all\n")).title()
           
        while month not in months:
            month=(input("Invalid Input,kindly type the month from the available data below:\nJanuary, February, March, April, May, June or all\n")).title()
        day=(input("kindly type the day from the available data below:\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all\n")).title()

        while day not in days:
            day=(input("Invalid Input kindly type the day from the available data below:\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all\n")).title()
###################################################################################
            
    else:
        month='All'
        day='All'
###################################################################################



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'All':
 
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day'].mode()[0]
    print('Most Popular Day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination']=df['Start Station']+' -> ' +df['End Station']
    
    popular_station = df['Combination'].mode()[0]
    print('Most Popular Starrt -> End Stations:', popular_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print('Total Travel Time: ',total_time)
    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('Total Mean Time: ',mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:\n\n',user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print('\nCounts of Gender:\n',user_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest=df['Birth Year'].min()
        max_recent=df['Birth Year'].max()
        most_common=df['Birth Year'].mode()[0]
    
        print('\nEarliest Year of Birth: ',earliest)
        print('Most Recent Year of Birth: ',max_recent)
        print('Most Common Year of Birth: ',most_common)
    if 'Birth Year' not in df.columns and 'Gender'  not in df.columns:
        print('\n\nSorry, there\'s no gender or birth year data for Washington')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
 # You can print a message like 
 print('\nRaw data is available to check... \n')

 # Then we follow a similar process of getting user input and taking action base on it, using the input function
 display_raw =input('May you want to have a look on the raw data? Type yes or no\n').lower()
 while display_raw != 'yes' and display_raw != 'no':
    display_raw =input('Invalid Input, May you want to have a look on the raw data? Type yes or no\n').lower()
 while display_raw == 'yes':
        try:
            chunksize=5
            for chunk in  pd.read_csv(CITY_DATA[city], chunksize = chunksize):
                print(chunk) 
                # repeating the question
                display_raw = input('May you want to have a look on the raw data? Type yes or no\n').lower()
                if display_raw != 'yes':
                    print('Thank You')
                    break
            break
        except KeyboardInterrupt:
            print('Thank you.')
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
