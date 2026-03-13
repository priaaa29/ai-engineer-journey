import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("clean_students.csv")
 #first 5 rows
print(df.head())

#average
df["Average"] = df[["Math","Science","English"]].mean(axis=1)
#rank
df["Rank"] = df[["Average"]].rank(ascending=false)
#top 5 students 
top_students = df.sort_values(by="Average" , ascending=false)
print(top_students[["Name","Average"]].head())

#weakest students 
weak_students = df.sort_values(by="Average")
print(weak_students[["Name","Average"]].head())

#hardest subject 
subject_avg = df[["Math","Science","English"]].mean()
print(subject_avg)

#visualise subject performance 
subject_avg.plot(kind="bar")

plt.title("Average Score by Subject")
plt.ylabel("Average Score")
plt.xlabel("Subject")

plt.show()

#correlation
corr = df[["Math","Science","English"]].corr()

print(corr)

#corr heatmap
sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Subject Correlation Heatmap")

plt.show()

#pass or fail
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")
print(df[["Name","Average","Result"]])

#pass or fail distribution
df["Result"].value_counts().plot(kind="bar")

plt.title("Pass vs Fail Distribution")

plt.show()

#grade wise performance 
grade_avg = df.groupby("Grade")["Average"].mean()

print(grade_avg)

#visualize
grade_avg.plot(kind="bar")

plt.title("Average Score by Grade")
plt.ylabel("Average Score")

plt.show()

print(df)