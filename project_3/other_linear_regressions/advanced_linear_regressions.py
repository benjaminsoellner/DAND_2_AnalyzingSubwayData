import numpy as np
import pandas as pd
import scipy
import statsmodels.api as sm
import datetime

"""
In this optional exercise, you should complete the function called 
predictions(turnstile_weather). This function takes in our pandas 
turnstile weather dataframe, and returns a set of predicted ridership values,
based on the other information in the dataframe.  

In exercise 3.5 we used Gradient Descent in order to compute the coefficients
theta used for the ridership prediction. Here you should attempt to implement 
another way of computing the coeffcients theta. You may also try using a reference implementation such as: 
http://statsmodels.sourceforge.net/devel/generated/statsmodels.regression.linear_model.OLS.html

One of the advantages of the statsmodels implementation is that it gives you
easy access to the values of the coefficients theta. This can help you infer relationships 
between variables in the dataset.

You may also experiment with polynomial terms as part of the input variables.  

The following links might be useful: 
http://en.wikipedia.org/wiki/Ordinary_least_squares
http://en.wikipedia.org/w/index.php?title=Linear_least_squares_(mathematics)
http://en.wikipedia.org/wiki/Polynomial_regression

This is your playground. Go wild!

How does your choice of linear regression compare to linear regression
with gradient descent computed in Exercise 3.5?

You can look at the information contained in the turnstile_weather dataframe below:
https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

Note: due to the memory and CPU limitation of our amazon EC2 instance, we will
give you a random subset (~10%) of the data contained in turnstile_data_master_with_weather.csv

If you receive a "server has encountered an error" message, that means you are hitting 
the 30 second limit that's placed on running your program. See if you can optimize your code so it
runs faster.
"""

def normalize(data):
    mean = data.mean()
    stdev = data.std()
    return (data-mean)/stdev

def predictions(weather_turnstile):
    weather_turnstile["is_weekend"] = weather_turnstile['DATEn'].map(lambda x: datetime.datetime.strptime(x, "%m-%d-%y").weekday() > 4)
    weather_turnstile["hour"]       = weather_turnstile['TIMEn'].map(lambda x: datetime.datetime.strptime(x, "%H:%M:%S").hour)
    
    # choose features
    num_variables = ['hour', 'meantempi', 'meanpressurei', 'meanprecipi', 'meanwspdi', 'is_weekend'] 
    exp_variables = [4, 2, 1, 1, 1, 1]
    cat_variables = ['conds', 'UNIT']
    res_variables = ['ENTRIESn_hourly']
    
    # Filter down to predictors & results, drop rows with empty data and duplicates
    filtered = weather_turnstile[num_variables+cat_variables+res_variables]
    filtered.is_copy = False
    filtered.dropna(inplace = True) # might not give us best model
    filtered.drop_duplicates(inplace = True) # might not give us best model
    
    # Handle numerical variables
    features = filtered[num_variables]
    print "========= Feature vector before normalization: ==========="
    print features.describe()
    features = normalize(features)
    # Try something with exponents (experimental)
    for i in range(0, len(num_variables)):
        v = num_variables[i]
        for e in range(2, exp_variables[i]+1):
            features[v+"_exp"+str(e)] = features[v]**e    
    print "========= Feature vector after normalization: ==========="
    print features.describe()
    
    # Handle categorical values
    for cat_variable in cat_variables:
        dummy_feature = pd.get_dummies(filtered[cat_variable], prefix=cat_variable)
        # Drop one column because of collinearity
        dummy_feature.drop(dummy_feature.columns[0], axis=1, inplace=True)
        features = features.join(dummy_feature)
    print "========= Analyzing mean precipitation data: ==========="
    analysis = pd.DataFrame( {"conds_Rain": features[features["conds_Rain"] == 1.0]["meanprecipi"].describe(), \
                              "conds_Heavy Rain": features[features["conds_Heavy Rain"] == 1.0]["meanprecipi"].describe(), \
                              "conds_Light Drizzle": features[features["conds_Light Drizzle"] == 1.0]["meanprecipi"].describe() } )
    print analysis

    # Add constant
    features = sm.add_constant(features)
    
    # Look out for multicollinearity - Watch out for strongly correlated features:
    
    # Get predictions
    values = filtered[res_variables]
    
    # Do linear regression
    result = sm.OLS(values, features).fit()
    prediction = result.predict(features)
    print result.summary()
    
    return prediction

def compute_r_squared(data, predictions):
    SST = ((data-np.mean(data))**2).sum()
    SSReg = ((predictions-np.mean(data))**2).sum()
    r_squared = SSReg / SST

    return r_squared

if __name__ == "__main__":
    input_filename = "turnstile_weather_v2.csv"
    turnstile_master = pd.read_csv(input_filename)
    predicted_values = predictions(turnstile_master)
    r_squared = compute_r_squared(turnstile_master['ENTRIESn_hourly'], predicted_values) 

    print r_squared