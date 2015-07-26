import pandas
import time

def time_to_hour(t):
    '''
    Given an input variable time that represents time in the format of:
    "00:00:00" (hour:minutes:seconds)
    
    Write a function to extract the hour part from the input variable time
    and return it as an integer. For example:
        1) if hour is 00, your code should return 0
        2) if hour is 01, your code should return 1
        3) if hour is 21, your code should return 21
        
    Please return hour as an integer.
    '''
    hour = time.strptime(t, "%H:%M:%S").tm_hour
    return hour

if __name__ == "__main__":
    input_filename = "turnstile_data_master_subset_consolidate_rows.csv"
    output_filename = "output.csv"
    turnstile_master = pandas.read_csv(input_filename)
    student_df = turnstile_master.copy(deep=True)
    student_df['Hour'] = student_df['TIMEn'].map(time_to_hour)
    student_df.to_csv(output_filename)