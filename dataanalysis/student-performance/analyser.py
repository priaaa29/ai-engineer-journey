import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("clean_students.csv")
 #first 5 rows
print(df.head())

#average
df["Average"] = df[["Math","Science","English"]].mean(axis=1)
print(df)