# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:06:20 2020

@author: Matthew.Walden
"""

import os
import pandas as pd
import time


directory = input("Please  enter the directory of the CSV files:\n")

while os.path.isdir(directory) == False:
    directory = input("Not Found! Please  enter the directory of the CSV files:\n")
os.chdir( '{directory}'.format(directory=directory) )




CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
DAY_DATA = {'all' : 0,
            'monday' : 1,
            'tuesday' : 2,
            'wednesday' : 3,
            'thursday': 4,
            'friday': 5,
            'saturday' : 6,
            'sunday' : 7}

MONTH_DATA = {'all' : 0,
              'january' : 1,
              'february' : 2,
              'march' : 3,
              'april' : 4,
              'may' : 5,
              'june' : 6,
              'july' : 7,
              'august' : 8,
              'september' : 9,
              'october' : 10,
              'november' : 11,
              'december' : 12}

CITIES = (list(CITY_DATA))
DAYS = list(DAY_DATA)
MONTHS = list(MONTH_DATA)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    global city
    city = input("Please  enter a city {CITIES}):\n".format(CITIES=CITIES))
    city = city.lower()
    while city not in CITIES:
        city = input("Error! Please enter a city {CITIES}):\n".format(CITIES=CITIES))
        city=city.lower()
    print('You entered {city}'.format(city=city))    
    # get user input for month (all, january, february, ... , june)
    global month
    month = input("Please enter a month {MONTHS}):\n".format(MONTHS=MONTHS))
    month = month.lower()
    while month not in MONTHS:
        month = input("Error! Please enter a month {MONTHS}):\n".format(MONTHS=MONTHS))
        month = month.lower()
    print('You entered {month}'.format(month=month))  
    # get user input for day of week (all, monday, tuesday, ... sunday)
    global day
    day = input("Please enter a day {DAYS}):\n".format(DAYS=DAYS))
    day = day.lower()
    while day  not in DAYS:
      day = input("Error! Please a day {DAYS}):\n".format(DAYS=DAYS))
      day = day.lower()     
    print('You entered {day}'.format(day=day))
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
# load data file into a dataframe
    filename = CITY_DATA[city.lower()]
    global df
    df = pd.read_csv(r'C:/Users/matthew.walden/Desktop/UdacityProjects/progs/datain/{filename}'.format(filename=filename))
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['weekday'] = pd.to_datetime(df['Start Time']).dt.day_name()
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    df['journey'] = df['Start Station'] + " to " + df['End Station']

    if day != 'all': 
        df = df[df.weekday == day]
    else:
        df = df       
    month_num=MONTH_DATA[month]   
    if month != 'all':
        df = df[df.month == month_num]
    else: 
        df = df       
    View_Req = input("Would you like to see a sample of the data? Enter yes or no:\n")  
    while View_Req.lower() != 'yes' and View_Req != 'no':
        View_Req = input("Error, please enter yes or no:\n") 
    n = 5
    while View_Req.lower() == 'yes':
        print(df.head(n))
        n += 5
        View_Req = input("Would you like to see more of the data? Enter yes or no:\n") 
        while View_Req.lower() != 'yes' and View_Req != 'no':
            View_Req = input("Error, please enter yes or no:\n") 
        print(df.head(n))
    print('Further rows not requested')

    return df
 
  



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if df.empty:
        print('Your Selection Has No Data, Time Stats Unavailable...')
    else:
    # display the most common month
        n = 1
        Popular_Month=df['month'].value_counts()[:n].index.tolist()
        Popular_Month=Popular_Month[0]
        pop_mon=(list(MONTH_DATA.keys())[list(MONTH_DATA.values()).index(Popular_Month)])  
        print('Most Popular Month:')
        print(pop_mon)
    # display the most common day of week
        Popular_Day=df['weekday'].value_counts()[:n].index.tolist()
        pop_day=Popular_Day[0]
        print('Most Popular Day:')
        print(pop_day)               
    # display the most common start hour
        Popular_Hour=df['hour'].value_counts()[:n].index.tolist()
        pop_hour=Popular_Hour[0]
        print('Most Popular Hour:')
        print(pop_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    if df.empty:
        print('Your Selection Has No Data, Station Stats Unavailable...')
    else:
    # display most commonly used start station
        n = 1
        Popular_Start=df['Start Station'].value_counts()[:n].index.tolist()
        Popular_Start=Popular_Start[0]
        print('Most Popular Starting Station:')
        print(Popular_Start)
    # display most commonly used end station
        Popular_End=df['End Station'].value_counts()[:n].index.tolist()
        Popular_End=Popular_End[0]
        print('Most Popular End Station:')
        print(Popular_End)
        print('Most Popular End Station:')
        print("No Data in Selection")
    # display most frequent combination of start station and end station trip
        Popular_Jour=df['journey'].value_counts()[:n].index.tolist()
        Popular_Jour=Popular_Jour[0]
        print('Most Popular Journey:')
        print(Popular_Jour)
        print('Most Popular Journey:')
        print("No Data in Selection")              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    if df.empty:
        print('Your Selection Has No Data, Trip Stats Unavailable...')
    else:
    # display total travel time
        Total_Time = df['Trip Duration'].sum()
        Total_Time = Total_Time/60
        print('Total Trip Duration:')
        print('{Total_Time} Mins'.format(Total_Time=Total_Time))
    # display mean travel time
        Mean_Time = df['Trip Duration'].mean()
        Mean_Time = Mean_Time/60
        print('Mean Trip Duration:')
        print('{Mean_Time} Mins'.format(Mean_Time=Mean_Time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def user_stats(df):
    """Displays statistics on bikeshare users."""
    start_time = time.time()

    print('\nCalculating User Stats...\n')    
    
    if df.empty:
        print('Your Selection Has No Data, User Stats Unavailable...')
    else:
    # Display counts of user types
        User_Counts = df['User Type'].value_counts()
        Subs = User_Counts.loc["Subscriber"] 
        Customers = User_Counts.loc["Customer"] 
        print('Subscribers: {Subs}'.format(Subs=Subs))
        print('Customers: {Customers}'.format(Customers=Customers))   
        # Display counts of gender
        Gender_Counts = df['Gender'].value_counts()
        Male = Gender_Counts.loc["Male"] 
        Female = Gender_Counts.loc["Female"] 
        print('Male: {Male}'.format(Male=Male))
        print('Female: {Female}'.format(Female=Female))   
    # Display earliest, most recent, and most common year of birth
        Max_YOB = df['Birth Year'].max()
        Max_YOB = int(Max_YOB)
        Min_YOB = df['Birth Year'].min()
        Min_YOB = int(Min_YOB)
        Common_YOB = df['Birth Year'].mode()
        Common_YOB = int(Common_YOB[0])
        print('Max Birth Year of birth: {Max_YOB}'.format(Max_YOB=Max_YOB))
        print('Min Birth Year of birth: {Min_YOB}'.format(Min_YOB=Min_YOB))
        print('Most Common Year of birth Year: {Common_YOB}'.format(Common_YOB=Common_YOB))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()



