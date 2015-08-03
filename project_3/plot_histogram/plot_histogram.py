import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histograph may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    
    plt.figure()
    binwidth = 1000
    data_norain  = turnstile_weather[turnstile_weather['rain']==0]['ENTRIESn_hourly']
    histo_norain = data_norain.hist(bins=range(int(min(data_norain)), int(max(data_norain) + binwidth), int(binwidth))) # your code here to plot a historgram for hourly entries when it is raining
    data_rain    = turnstile_weather[turnstile_weather['rain']==1]['ENTRIESn_hourly']
    histo_rain   = data_rain.hist(bins=range(int(min(data_rain)), int(max(data_rain) + binwidth), int(binwidth))) # your code here to plot a historgram for hourly entries when it is raining
    histo_rain.set_xlabel('Hourly Average')
    histo_rain.set_xlim([0,25000])
    histo_rain.set_ylabel('Number of Days')
    plt.suptitle('Histogram of Hourly Riders on Rainy vs. Not-Rainy Days')
    return plt


if __name__ == "__main__":
    image = "plot.png"
    turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
    plt = entries_histogram(turnstile_weather)
    plt.savefig(image)