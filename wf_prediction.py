import joblib

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.svm import SVR

# Linear Regression


def test1(x_test, y_test, name):
    model = joblib.load("models\linear_regression.joblib")

    y_pred = model.predict(x_test)

    return y_pred,name
# Lasso Regression


def test2(x_test, y_test, name, model):

    y_pred = model.predict(x_test)

    return y_pred,name

# Ridge Regression


def test3(x_test, y_test, name, model):

    y_pred = model.predict(x_test)

    return y_pred,name

def test5(x_test, y_test, name):
    model = joblib.load("models\decision_tree.joblib")

    y_pred = model.predict(x_test)

    return y_pred,name

def test6(x_test, y_test, name):
    model = joblib.load("models\\random_forest.joblib")

    y_pred = model.predict(x_test)

    return y_pred,name
    