import pandas as pd
df=pd.read_csv(r"D:\Student Performance\archive\StudentsPerformance.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)