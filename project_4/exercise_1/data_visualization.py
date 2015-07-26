import pandas as pd
import datetime
from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    turnstile_weather.is_copy = False
    
    # Add column for weekday 0-6
    turnstile_weather["weekday"] = turnstile_weather['DATEn'].map(lambda x: datetime.strptime(x, "%Y-%m-%d").weekday())
    # Group by weekday
    summary = turnstile_weather.groupby(["weekday"], as_index=False)["ENTRIESn_hourly"].mean()
    # Re-label list for later
    label_list = [ '', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Plot with day of week relabeled as abreviation
    plot = ggplot(summary, aes('weekday', 'ENTRIESn_hourly')) + \
        geom_bar(stat='identity', fill='blue') + \
        xlab('Weekday') + \
        ylab('Average Entries per Hour') + \
        ggtitle('Subway entries by day of week') + \
        scale_x_discrete(labels=label_list)
    
    return plot



if __name__ == "__main__":
    image = "plot.png"
    with open(image, "wb") as f:
        turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
        turnstile_weather['datetime'] = turnstile_weather['DATEn'] + ' ' + turnstile_weather['TIMEn']
        gg =  plot_weather_data(turnstile_weather)
        ggsave(image, gg)
