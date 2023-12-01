import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Linear Regression


def model1(x_train, y_train):
    model1 = LinearRegression()
    model1.fit(x_train, y_train)

    joblib.dump(model1, "models\linear_regression.joblib")

# Lasso Regression


def model2(model):
    joblib.dump(model, "models\lasso_regression_version.joblib")

# Ridge Regression


def model3(model):
    joblib.dump(model, "models\\ridge_regression_version.joblib")

def model5(x_train, y_train):
    model5 = DecisionTreeRegressor()
    # y_train = y_train.values.ravel()
    model5.fit(x_train, y_train)

    joblib.dump(model5, "models\decision_tree.joblib")

def model6(x_train, y_train):
    model6 = RandomForestRegressor()
    # y_train = y_train.values.ravel()
    model6.fit(x_train, y_train)

    joblib.dump(model6, "models\\random_forest.joblib")

def model7(x_train, y_train, x2):
    model = LinearRegression()
    model.fit(x_train, y_train)
    y2 = model.predict(x2)

    return y2
