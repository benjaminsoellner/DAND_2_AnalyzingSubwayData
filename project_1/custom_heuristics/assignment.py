import numpy
import pandas
import math
import statsmodels.api as sm

def custom_heuristic(file_path):
    '''
    You are given a list of Titantic passengers and their associated
    information. More information about the data can be seen at the link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data

    For this exercise, you need to write a custom heuristic that will take
    in some combination of the passenger's attributes and predict if the passenger
    survived the Titanic diaster.

    Can your custom heuristic beat 80% accuracy?
    
    The available attributes are:
    Pclass          Passenger Class
                    (1 = 1st; 2 = 2nd; 3 = 3rd)
    Name            Name
    Sex             Sex
    Age             Age
    SibSp           Number of Siblings/Spouses Aboard
    Parch           Number of Parents/Children Aboard
    Ticket          Ticket Number
    Fare            Passenger Fare
    Cabin           Cabin
    Embarked        Port of Embarkation
                    (C = Cherbourg; Q = Queenstown; S = Southampton)
                    
    SPECIAL NOTES:
    Pclass is a proxy for socioeconomic status (SES)
    1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower

    Age is in years; fractional if age less than one
    If the age is estimated, it is in the form xx.5

    With respect to the family relation variables (i.e. SibSp and Parch)
    some relations were ignored. The following are the definitions used
    for SibSp and Parch.

    Sibling:  brother, sister, stepbrother, or stepsister of passenger aboard Titanic
    Spouse:   husband or wife of passenger aboard Titanic (mistresses and fiancees ignored)
    Parent:   mother or father of passenger aboard Titanic
    Child:    son, daughter, stepson, or stepdaughter of passenger aboard Titanic
    
    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associating value should be 1 if the
    passenger survvied or 0 otherwise. 

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
        (lambda x: ( ((x['Sex'] == 'Female') | (x['Sex'] == 'female')) & ((x['Pclass'] != 3) | (x['Age'] < 35) | (x['SibSp'] + x['Parch'] == 0))
                    | ((x['Pclass'] == 1) & (x['Age'] < 18))
                    #| (not isinstance(x['Cabin'], float) or not numpy.isnan(x['Cabin']))
                    )),
        axis=1 )
    print isinstance(df[df['Cabin'].isnull()]['Cabin'][0], float) and not numpy.isnan(df[df['Cabin'].isnull()]['Cabin'][0])
    print 'Number of survivors acc. heuristic: ' + df[df['Heuristic'] == True]['PassengerId'].count().astype(str)
    print 'Actual number of survivors:         ' + df[df['Survived'] == True]['PassengerId'].count().astype(str)
    print 'False positives:                    ' + df[(df['Survived'] == False) & (df['Heuristic'] == True)]['PassengerId'].count().astype(str)
    print df[(df['Survived'] == False) & (df['Heuristic'] == True)]
    print 'False negatives:                    ' + df[(df['Survived'] == True) & (df['Heuristic'] == False)]['PassengerId'].count().astype(str)
    print df[(df['Survived'] == True) & (df['Heuristic'] == False)]
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
    predictions = custom_heuristic(file_name)
    for row_index, row in df.iterrows():
        total_count += 1
        if predictions[row['PassengerId']] == row['Survived']:
            correct_count += 1
    return correct_count/total_count


if __name__ == "__main__":
    custom_heuristic_success_rate = check_accuracy('titanic_data.csv')
    print custom_heuristic_success_rate 