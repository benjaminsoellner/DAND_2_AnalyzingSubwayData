import datetime
import time
import pandas as pd

def reformat_subway_dates(d):
    '''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-day.
    
    In order to join these two data sets together, we'll want the dates formatted
    the same way.  Write a function that takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.
    
    Hint: 
    There are a couple of useful functions in the datetime library that will
    help on this assignment, called strptime and strftime. 
    More info can be seen here and further in the documentation section:
    http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
    '''

    date_formatted = datetime.datetime.strptime(d, "%m-%d-%y").strftime("%Y-%m-%d")
    return date_formatted

if __name__ == "__main__":
    input_filename = "turnstile_data_master_subset_time_to_hours.csv"
    output_filename = "output.csv"

    turnstile_master = pd.read_csv(input_filename)
    student_df = turnstile_master.copy(deep=True)
    student_df['DATEn'] = student_df['DATEn'].map(reformat_subway_dates)
    student_df.to_csv(output_filename) 