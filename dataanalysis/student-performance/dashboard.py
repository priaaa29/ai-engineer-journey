import streamlit as st
import pandas as pd

st.title("Student Performance Analyzer")

df = pd.read_csv("clean_students.csv")

st.write(df.head())