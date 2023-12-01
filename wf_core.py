import pandas as pd
from wf_dataprocessing import processing
from wf_visualization import visualize



input_file=pd.read_csv("data_original\ct.csv")
df=pd.DataFrame(input_file[3:])

processing(df)

input_file=pd.read_csv("data_processed\quarterly.csv")
df=pd.DataFrame(input_file)
visualize(df)

