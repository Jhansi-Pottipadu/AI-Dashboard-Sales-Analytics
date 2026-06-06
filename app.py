import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Restaurant Tips Dashboard", layout="wide")

# Load Dataset
df = pd.read_csv("dataset.csv")

# Data Cleaning
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

st.title("AI Dashboard - Restaurant Tips Analysis")

# Dataset Overview
st.header("Dataset Overview")

st.write("Number of Rows:", df.shape[0])
st.write("Number of Columns:", df.shape[1])

st.dataframe(df.head())

# Data Cleaning Report
st.header("Data Cleaning")

st.write("Missing Values")

st.write(df.isnull().sum())

# Filters
st.sidebar.header("Interactive Filters")

gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["sex"].unique(),
    default=df["sex"].unique()
)

day = st.sidebar.multiselect(
    "Select Day",
    options=df["day"].unique(),
    default=df["day"].unique()
)

filtered_df = df[
    (df["sex"].isin(gender)) &
    (df["day"].isin(day))
]

# KPIs
st.header("Key Metrics (KPIs)")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Bills", round(filtered_df["total_bill"].sum(), 2))

col2.metric("Total Tips", round(filtered_df["tip"].sum(), 2))

col3.metric("Average Bill", round(filtered_df["total_bill"].mean(), 2))

col4.metric("Average Tip", round(filtered_df["tip"].mean(), 2))

# Visualization 1
st.header("Visualization 1 - Total Bills by Day")

fig1 = px.bar(
    filtered_df.groupby("day")["total_bill"].sum().reset_index(),
    x="day",
    y="total_bill"
)

st.plotly_chart(fig1, use_container_width=True)

# Visualization 2
st.header("Visualization 2 - Gender Distribution")

fig2 = px.pie(
    filtered_df,
    names="sex"
)

st.plotly_chart(fig2, use_container_width=True)

# Visualization 3
st.header("Visualization 3 - Tips Distribution")

fig3 = px.histogram(
    filtered_df,
    x="tip"
)

st.plotly_chart(fig3, use_container_width=True)

# Visualization 4
st.header("Visualization 4 - Total Bill vs Tip")

fig4 = px.scatter(
    filtered_df,
    x="total_bill",
    y="tip",
    color="sex"
)

st.plotly_chart(fig4, use_container_width=True)

# Visualization 5
st.header("Visualization 5 - Smoker Analysis")

fig5 = px.box(
    filtered_df,
    x="smoker",
    y="tip"
)

st.plotly_chart(fig5, use_container_width=True)
st.header("Business Insights")

st.write("1. Higher bills generally produce higher tips.")
st.write("2. Weekend days generate more restaurant revenue.")
st.write("3. Customer tipping behavior varies by gender and smoking status.")
st.write("4. Interactive filters help analyze customer segments.")