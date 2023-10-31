import pandas as pd
import numpy as np

input_file=pd.read_csv("data_original\ct.csv")
df=pd.DataFrame(input_file[3:])

df=df[~df['Household final consumption expenditure: National concept IDEF SA 2019=100'].isnull()]
df=df[~df['Household final consumption expenditure: National concept IDEF NSA 2019=100'] .isnull()]

x=np.array(df)

a=[]
b=[]

for i in x:
    if np.char.isnumeric(i[0]):
        a.append(i)
    else:
        b.append(i)

a=pd.DataFrame(a)
b=pd.DataFrame(b)

a.columns=df.columns

b.columns=df.columns

df.to_csv('data_processed\entire.csv')

a.to_csv('data_processed\yearly.csv')

b.to_csv('data_processed\quarterly.csv')