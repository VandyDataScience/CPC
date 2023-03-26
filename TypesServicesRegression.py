import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def runModel (activity) : 
    # upload data 
    df = pd.read_csv('CentennialReal.csv')

    # extract only the locals from the data frame
    local = df.loc[(df["How far do you travel to get to the Park?"]=="Less than a mile away") | (df["How far do you travel to get to the Park?"]=="6 - 9 miles away") | (df["How far do you travel to get to the Park?"]=="1 - 5 miles away")]

    # set up the input variables 
    X = local[["How often do you visit Centennial Park?", "What is your age?", "What is your gender?"]]
    X = pd.get_dummies(data=X, drop_first=True)
    
    # create new column based on if someone wants specific activity/service 
    local = local.assign(column = [1 if str(a).__contains__(activity) else 0 for a in local["If yes, which activities or services would you most like to see? (select all that apply)"]])

    y = local["column"]

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Create the logistic regression model
    model = LogisticRegression()

    # Train the model on the training set
    model.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = model.predict(X_test)
    print('Predictions: ', y_pred)

    # Evaluate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy: ', accuracy)

    
runModel("Event")
runModel("food and beverage")