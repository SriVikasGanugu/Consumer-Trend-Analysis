import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from wf_training import model1
from wf_training import model2
from wf_training import model3
from wf_training import model5
from wf_training import model6
from wf_training import model7

from wf_prediction import test1
from wf_prediction import test2
from wf_prediction import test3
from wf_prediction import test5
from wf_prediction import test6

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

from sklearn.linear_model import Lasso, Ridge

def evaluate_model(name, y_test, y_pred, entire):
    mae = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    result_str = f"Model Evaluation: {name}\nMSE: {mae}\nR-squared: {r2}\n\n"

    entire += result_str
    return entire


f1 = pd.read_csv("data_processed/yearly.csv")
d1 = pd.DataFrame(f1)
d1['Household final consumption expenditure: National concept IDEF NSA 2019=100'] *= 4
d1 = d1.drop(d1.columns[0], axis=1)
d1['Title'] = d1['Title'].astype(str)

f2 = pd.read_csv("data_processed/quarterly.csv")
d2 = pd.DataFrame(f2)
d2 = d2.drop(d2.columns[0], axis=1)

l1 = np.asanyarray(d1)
l2 = np.asanyarray(d2)

l1[:, 1:] /= 4

a = np.array([])
l = np.array([])

cE_inc = []
yr = []
ini = l1[0][8]

for i in range(len(l2)):
    if (i) % 4 == 0:
        a = np.append(a, l1[((i+1)//4)-1])
        cE_inc.append(a[8]-ini)
        yr.append(a[0])
        ini = a[8]
    a = np.append(a, l2[i])
    l = np.append(l, a)
    a = []
l = l.reshape(-1, l2.shape[1])

c = pd.DataFrame(l)
c.columns = d1.columns


def change(value):
    l = value.split(' ')
    result = 0
    year = int(l[0])
    if len(l) == 2:
        quarter = int(l[1][1])  # Extract the numeric part of the quarter
        result = year + (quarter-1) * 0.2
    else:
        result = year+0.8
    return result


c['Title'] = c['Title'].apply(change)
c.to_csv('data_processed\data_set.csv')

test_size = 30/len(l)
split_index = int(len(l) * test_size)

corr = c.corr()

corr.to_csv('data_processed\correlation_matrix.txt',
            sep='\t', float_format='%.4f')
corr_list = [(i, j, corr.loc[i, j])
             for i in c.columns for j in c.columns if i != j]
corr_list = sorted(corr_list, key=lambda x: abs(x[2]))
s_features = corr_list[:20]

# X set
names = []
for i in s_features:
    if i[0] not in names:
        names.append(i[0])
    if i[1] not in names:
        names.append(i[1])

# Y Set
y_name = [
    'Household final consumption expenditure: National concept IDEF NSA 2019=100'
]

x_train, x_test, y_train, y_test = train_test_split(
    c[names], c[y_name], test_size=test_size, random_state=42)

# Training
# INITIAL MODEL
entire = ""
pred = 0

model1(x_train, y_train)
y_pred, name = test1(x_test, y_test, "Linear_Regression")
pred = y_pred
entire = evaluate_model(name, y_test, y_pred, entire)

model = joblib.load("models\linear_regression.joblib")

m_ver1 = Lasso(0.1)
m_ver1.coef = model.coef_
m_ver1.fit(x_train, y_train)
model2(m_ver1)

y_pred, name = test2(
    x_test, y_test, "Lasso_Regression(Alternate Version)", m_ver1)

entire = evaluate_model(name, y_test, y_pred, entire)


m_ver2 = Ridge(0.1)
m_ver2.coef = model.coef_
m_ver2.fit(x_train, y_train)
model3(m_ver2)

y_pred, name = test3(
    x_test, y_test, "Ridge_Regression(Alternate Version)", m_ver2)

entire = evaluate_model(name, y_test, y_pred, entire)

model5(x_train, y_train)
y_pred, name = test5(x_test, y_test, "Decision_Tree")

entire = evaluate_model(name, y_test, y_pred, entire)

model6(x_train, y_train)
y_pred, name = test6(x_test, y_test, "Random_Forest")

entire = evaluate_model(name, y_test, y_pred, entire)

with open('evaluation/'+'summary'+'.txt', 'a') as file:
    file.write(entire)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))

sns.scatterplot(x='Semi-durable goods: Total IDEF NSA 2019=100',
                y='Household final consumption expenditure: National concept IDEF NSA 2019=100', data=c, ax=axes[0, 0])
axes[0, 0].set_title('Feature A Alone')

# Plot for Feature B (UK tourist expenditure abroad) alone
sns.scatterplot(x='Household final consumption expenditure: UK tourist expenditure abroad CVM NSA £m',
                y='Household final consumption expenditure: National concept IDEF NSA 2019=100', data=c, ax=axes[0, 1])
axes[0, 1].set_title('Feature B Alone')

# Plot for both features A and B correlated
sns.scatterplot(x='Semi-durable goods: Total IDEF NSA 2019=100',
                y='Household final consumption expenditure: UK tourist expenditure abroad CVM NSA £m', data=c, ax=axes[1, 0])
axes[1, 0].set_title('Both Features Correlated')

# Plot for both features A and B inversely related
sns.scatterplot(x='Semi-durable goods: Total IDEF NSA 2019=100',
                y='Household final consumption expenditure: UK tourist expenditure abroad CVM NSA £m', data=c[::-1], ax=axes[1, 1])
axes[1, 1].set_title('Both Features Inversely Related')

plt.tight_layout()
plt.savefig("visuals\\feature_trends.png")
plt.show()

f = c[:115]

x_train, x_test, y_train, y_test = train_test_split(
    f['Title'], f['Household final consumption expenditure: National concept IDEF NSA 2019=100'], test_size=0.2)
x_train = x_train.values.reshape(-1, 1)
x_test = x_test.values.reshape(-1, 1)
x2 = c[115:]['Title'].values.reshape(-1, 1)
y2 = model7(x_train, y_train, x2)

plt.scatter(c[115:]['Title'], c[115:]['Household final consumption expenditure: National concept IDEF NSA 2019=100'],
            color="Red", label="Actual HFCE")
plt.plot(c[115:]['Title'], y2, color="Blue", label="Predicted HCFE")

plt.title('Scatter Plot: Year vs. HFCE')
plt.xlabel('Year')
plt.ylabel('Household Final Consumption Expenditure (HFCE)')
plt.savefig("visuals\\year_Expenditure.png")
plt.show()

plt.scatter(c['Title'], c['Household final consumption expenditure: National concept IDEF NSA 2019=100'],
            color="Red", label="Actual HFCE")
plt.title('Consumer Trends in UK(per Quarter)')
plt.xlabel('Year')
plt.ylabel('Final Consumption Expenditure')
plt.savefig("visuals\\inflation.png")
plt.show()


plt.scatter(yr, cE_inc)
plt.title('Increase in Consumer Expenditure per year')
plt.xlabel('Year')
plt.ylabel('Increase in Consumption Expenditure')
plt.savefig("visuals\\consumption_increase.png")
plt.show()

