import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("marksheet.csv.csv")

#see top 5 rows of data
# print(df.head())

# change names to proper format 
df["Name"] = df["Name"].str.replace("'", "")
df["Name"] = df["Name"].str.replace('"', "")
df["Name"] = df["Name"].str.strip()
df["Name"] = df["Name"].str.title()

#gender formatting
df["Gender"] = df["Gender"].astype(str).str.strip().str.lower()

gender_map = { 
    "M" : "Male",
    "m" : "Male",
    "0" : "Male",
    "male" : "Male",
    "Male" : "Male",
    "F" : "Female",
    "f" : "Female",
    "1" : "Female",
    "female" : "Female",
    "Female" : "Female"
}
df["Gender"] = df["Gender"].map(gender_map)

#grade column 
df["Grade"] = df["Grade"].astype(str)
df["Grade"] = df["Grade"].str.replace("Grade","")
df["Grade"] = df["Grade"].str.strip()
df["Grade"] = pd.to_numeric(df["Grade"])

#marks column fix 
for col in ["Math","Science","English"] :
    df[col] = df[col].astype(str).str.replace("marks","")
    df[col] = df[col].str.strip()
    df[col] = pd.to_numeric(df[col])

#recalculate total
df["Total"] = df["Math"] + df["Science"] + df["English"]


# find duplicate values
print(df.duplicated().sum())  
#result = 0 that means no duplicate values 

# #see data info
print(df.info())

print(df)

# save the clean dataset
df.to_csv("clean_students.csv", index=False)