# -*- coding: utf-8 -*-
"""Copy of Classification Model to Identify Multiple Disease Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13zMlCZ5IHc69fr_DNbSae0wR-qfTA1G4

# **⭐ Classification Model to Identify Multiple Disease**
"""

# import library
import pandas as pd

# import data
disease = pd.read_csv('https://github.com/ybifoundation/Dataset/raw/main/MultipleDiseasePrediction.csv')

# view data
disease.head()

# info of data
disease.info()

# summary statistics
disease.describe()

# check for missing value
disease.isna().sum()

# check for categories
disease.nunique()

# correlation
disease.corr()

# column names
disease.columns

# define y
y = disease['prognosis']

# define X
x = disease.drop(['prognosis'],axis=1)

# split data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=2559)

# verify shape
disease.shape, y.shape, x.shape

# select model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

# train model
model.fit(x_train,y_train)

# predict with model
y_pred = model.predict(x_test)

# model evaluation
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# model accuracy
accuracy_score(y_test,y_pred)

# model confusion matrix
print(confusion_matrix(y_test,y_pred))

# model classification report
print(classification_report(y_test,y_pred))

# future prediction
x_new = x.sample()

# define X_new
x_new

# predict for X_new
model.predict(x_new)

