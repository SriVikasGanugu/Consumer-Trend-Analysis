import pandas as pd
import numpy as np


def processing(df):
    df = df[~df['Household final consumption expenditure: National concept IDEF SA 2019=100'].isnull()]
    df = df[~df['Household final consumption expenditure: National concept IDEF NSA 2019=100'] .isnull()]

    x = np.array(df)

    a = []
    b = []

    for i in x:
        if np.char.isnumeric(i[0]):
            a.append(i)
        else:
            b.append(i)

    a = pd.DataFrame(a)
    b = pd.DataFrame(b)

    a.columns = df.columns

    b.columns = df.columns

    df.to_csv('data_processed\entire.csv')
    a.to_csv('data_processed\yearly.csv')
    b.to_csv('data_processed\quarterly.csv')

    f1 = pd.read_csv("data_processed/yearly.csv")
    d1 = pd.DataFrame(f1)
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
    for i in range(len(l2)):
        if (i+1) % 4 == 0:
            a = np.append(a, l1[((i+1)//4)-1])
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
            quarter = int(l[1][1])
            result = year + (quarter-1) * 0.2
        else:
            result = year+0.8
        return result

    c['Title'] = c['Title'].apply(change)

    c.to_csv('data_processed\data_set.csv')
