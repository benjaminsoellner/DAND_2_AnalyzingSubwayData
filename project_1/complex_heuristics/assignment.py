import numpy
import pandas
import statsmodels.api as sm

def complex_heuristic(file_path):
    '''
    You are given a list of Titantic passengers and their associated
    information. More information about the data can be seen at the link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data

    For this exercise, you need to write a more sophisticated algorithm
    that will use the passengers' gender and their socioeconomical class and age 
    to predict if they survived the Titanic diaster. 
    
    You prediction should be 79% accurate or higher.
    
    Here's the algorithm, predict the passenger survived if:
    1) If the passenger is female or
    2) if his/her socioeconomic status is high AND if the passenger is under 18
    
    Otherwise, your algorithm should predict that the passenger perished in the disaster.
    
    Or more specifically in terms of coding:
    female or (high status and under 18)
    
    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger['Sex'] will return a string "female".
    
    You can access the socioeconomic status of a passenger via passenger['Pclass']:
    High socioeconomic status -- passenger['Pclass'] is 1
    Medium socioeconomic status -- passenger['Pclass'] is 2
    Low socioeconomic status -- passenger['Pclass'] is 3

    You can access the age of a passenger via passenger['Age'].
    
    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the Passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associated value should be 1 if the
    passenger survived or 0 otherwise. 

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
        (lambda x: ((x['Sex'] == 'Female') | (x['Sex'] == 'female') | ((x['Pclass'] == 1) & (x['Age'] < 18)))),
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
    predictions = complex_heuristic(file_name)
    for row_index, row in df.iterrows():
        total_count += 1
        if predictions[row['PassengerId']] == row['Survived']:
            correct_count += 1
    return correct_count/total_count


if __name__ == "__main__":
    complex_heuristic_success_rate = check_accuracy('titanic_data.csv')
    print complex_heuristic_success_rate
    