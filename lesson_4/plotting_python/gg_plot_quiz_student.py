import matplotlib
matplotlib.use('agg')

import pandas as pd
from ggplot import *

def lineplot(hr_year_csv):
    # A csv file will be passed in as an argument which
    # contains two columns -- 'HR' (the number of homerun hits)
    # and 'yearID' (the year in which the homeruns were hit).
    #
    # Fill out the body of this function, lineplot, to use the
    # passed-in csv file, hr_year.csv, and create a
    # chart with points connected by lines, both colored 'red',
    # showing the number of HR by year.
    #
    # You will want to first load the csv file into a pandas dataframe
    # and use the pandas dataframe along with ggplot to create your visualization
    #
    # You can check out the data in the csv file at the link below:
    # https://www.dropbox.com/s/awgdal71hc1u06d/hr_year.csv
    #
    # You can read more about ggplot at the following link:
    # https://github.com/yhat/ggplot/
    
    hr_df = pd.read_csv(hr_year_csv)
    gg = ggplot(hr_df, aes('yearID', 'HR')) + geom_point(color='red') + geom_line(color='red') + ggtitle('Total HRs by Year') + xlab('Year') + ylab('HR')
    return gg

if __name__ == "__main__":
    data = "hr_year.csv"
    image = "plot.png"
    gg =  lineplot(data)
    ggsave(image, gg, width=11, height=8)