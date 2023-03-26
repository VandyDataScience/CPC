from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.metrics import accuracy_score

# upload data 
df = pd.read_csv('CentennialReal.csv')

# extract only the locals from the data frame
local = df.loc[(df["How far do you travel to get to the Park?"]=="Less than a mile away") | (df["How far do you travel to get to the Park?"]=="6 - 9 miles away") | (df["How far do you travel to get to the Park?"]=="1 - 5 miles away")]

# create input data frame of input data and set up dummy variables
X = local[["How often do you visit Centennial Park?", "What is your age?", "What is your gender?"]]
X = pd.get_dummies(data=X, drop_first=True)
X.head()

# set up output data with dummy variables
Y = local["Do you believe the Park could benefit from more ongoing activities or services?"]
Y = pd.get_dummies(data=Y, drop_first=True)

# run linear regression with train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=101)
model = LogisticRegression().fit(X_train, y_train)

# make predictions
predictions = model.predict(X_test)
print(predictions)

# look at summary of model
X_train_Sm= sm.add_constant(X_train)
X_train_Sm= sm.add_constant(X_train)
ls=sm.OLS(y_train,X_train_Sm).fit()
print(ls.summary())

# look at accuracy of model
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: ", accuracy)
