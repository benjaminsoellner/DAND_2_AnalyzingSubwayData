import numpy
import pandas
import statsmodels.api as sm

def simple_heuristic(file_path):
    '''
    In this exercise, we will perform some rudimentary practices similar to those of
    an actual data scientist.
    
    Part of a data scientist's job is to use her or his intuition and insight to
    write algorithms and heuristics. A data scientist also creates mathematical models 
    to make predictions based on some attributes from the data that they are examining.

    We would like for you to take your knowledge and intuition about the Titanic
    and its passengers' attributes to predict whether or not the passengers survived
    or perished. You can read more about the Titanic and specifics about this dataset at:
    http://en.wikipedia.org/wiki/RMS_Titanic
    http://www.kaggle.com/c/titanic-gettingStarted
        
    In this exercise and the following ones, you are given a list of Titantic passengers
    and their associated information. More information about the data can be seen at the 
    link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data. 

    For this exercise, you need to write a simple heuristic that will use
    the passengers' gender to predict if that person survived the Titanic disaster.
    
    You prediction should be 78% accurate or higher.
        
    Here's a simple heuristic to start off:
       1) If the passenger is female, your heuristic should assume that the
       passenger survived.
       2) If the passenger is male, you heuristic should
       assume that the passenger did not survive.
    
    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger['Sex'] will return a string "female".

    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associated value should be 1 if the
    passenger survied or 0 otherwise.

    For example, if a passenger is predicted to have survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    And if a passenger is predicted to have perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0
    
    You can also look at the Titantic data that you will be working with
    at the link below:
    https://www.dropbox.com/s/r5f9aos8p9ri9sa/titanic_data.csv
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    df['Heuristic'] = df.apply(
        (lambda x: ((x['Sex'] == 'Female') | (x['Sex'] == 'female'))), 
        axis=1 )
    print 'Number of survivors acc. heuristic: ' + df[df['Heuristic'] == True]['PassengerId'].count().astype(str)
    print 'Actual number of survivors:         ' + df[df['Survived'] == True]['PassengerId'].count().astype(str)
    print 'False positives:                    ' + df[(df['Survived'] == False) & (df['Heuristic'] == True)]['PassengerId'].count().astype(str)
    print 'False negatives:                    ' + df[(df['Survived'] == True) & (df['Heuristic'] == False)]['PassengerId'].count().astype(str)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        predictions[passenger_id] = passenger['Heuristic']
        # Your code here:
        # For example, let's assume that if the passenger
        # is a male, then the passenger survived.
        #     if passenger['Sex'] == 'male':
        #         predictions[passenger_id] = 1
        
    return predictions

def check_accuracy(file_name):
    total_count = 0
    correct_count = 0
    df = pandas.read_csv(file_name)
    predictions = simple_heuristic(file_name)
    for row_index, row in df.iterrows():
        total_count += 1
        if predictions[row['PassengerId']] == row['Survived']:
            correct_count += 1
    return correct_count/total_count

if __name__ == "__main__":
    simple_heuristic_success_rate = check_accuracy('titanic_data.csv')
    print simple_heuristic_success_rate
    