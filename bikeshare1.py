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
  
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please choose a city from chicago, new york city, washington : ").lower()
        if city not in CITY_DATA:
            print("Invalid input. Enter the correct city name")
        else:
            break
           
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter a month from januaey to june or type 'all' to display all months : ").lower()
        months = ['january','february','march','april','may','june']
        if month != 'all' and (month not in months):
            print("Please enter a valid month name")
        else:
            break
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the day of the week or type 'all' to display data for all days of a week: ").lower()
        days= ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        if(day != 'all') and (day not in days):
            print ('Invalid input. Enter a valid day')
        else:
            break
            
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
    df['Start Time'] = pd.to_datetime(df["Start Time"])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april',' may' , 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df

def display_raw_data(df):
    """
    Displays subsequent rows of data according to user answer

    Args:
            df - Pandas DataFrame containing city data filtered by month and day returned from load_data() function
    """
    
    i = 0
    answer = input('Would you like to display first 5 rows of data? yes/no: ').lower()
    pd.set_option('display.max_columns', None)
    
    while True:
        if answer == 'no':
            break
        print (df[i:i+5])
        answer = input('would you like to display the next 5 rows of data? yes/no: ').lower()
        i+=5
  

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode() [0]
    print(common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.week
    common_day_of_week = df['day_of_week'].mode() [0]
    print(common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print(common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode() [0]
    print(common_start)


    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode() [0]
    print(common_end)


    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station'] + ' - ' + df['End Station']) . mode()[0]
    print(" The most frequent combination of start station and end station trip is: " , common_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print(user_types_count)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print (gender)
    else:
        print("No data available.")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = int(df['Birth_Year'] .min())
        print(earliest)
        most_recent = int(df['Birth_Year'].max())
        print(most_recent)
        most_common = int(df['Birth_Year'].mode()[0])
        print (most_common)
    else:
        print("No information available.")
   
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    
    
