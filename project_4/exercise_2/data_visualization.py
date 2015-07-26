from pandas import *
from ggplot import *
from pandas import *
from ggplot import *
import pandas as pd

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
    
    # Group by Unit and get average entries and exits for that unit
    df_grouped           = turnstile_weather.groupby(["UNIT"], as_index=False)["EXITSn_hourly", "ENTRIESn_hourly"].mean()
    df_grouped.is_copy   = False
    # Filter out all values where entries or exits is 0
    df_filtered          = df_grouped[(df_grouped["ENTRIESn_hourly"] != 0.0) & (df_grouped["EXITSn_hourly"] != 0.0)]
    df_filtered.is_copy  = False
    # Calculate ratio of entries / exits
    df_filtered["ratio"] = df_filtered["ENTRIESn_hourly"]/df_filtered["EXITSn_hourly"]
    # Sort by ratio
    df_sorted            = df_filtered.sort("ratio")
    # Get top and bottom 10 
    df_head_and_tail     = concat([df_sorted.head(10), df_sorted.tail(10)]).reset_index()

    print df_head_and_tail

    # Plot as bar graph
    plot = ggplot(df_head_and_tail, aes(x='UNIT', y='ratio')) + \
        geom_bar(stat='identity', fill='blue') + \
        ggtitle('10 Stations With the Lowest (Left) & Highest (Right) Number of Entries vs. Exits') + \
        scale_x_discrete() + \
        xlab('Subway Station') + \
        ylab('Ratio of Entries/Exits') + \
        scale_y_continuous(limits = (0, 100)) + \
        theme(axis_text_x = element_text(angle = 90, hjust = 1))
    
    return plot

if __name__ == "__main__":
    image = "plot.png"
    with open(image, "wb") as f:
        turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
        turnstile_weather['datetime'] = turnstile_weather['DATEn'] + ' ' + turnstile_weather['TIMEn']
        gg =  plot_weather_data(turnstile_weather)
        ggsave(image, gg)