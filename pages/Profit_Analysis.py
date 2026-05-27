import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Profit Analysis", layout="wide")

@st.cache_data
def read_excel(file):
    df = pd.read_excel(file)
    return df

df = read_excel("data/sales.xls")
st.subheader("Profit Analysis")

if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month_name()
    df["Month Number"] = df["Order Date"].dt.month
    df["Year Month"] = df["Order Date"].dt.to_period("M").astype(str)



if "Profit" in df.columns:

    total_profit = df["Profit"].sum()
    avg_profit = df["Profit"].mean()
    max_profit = df["Profit"].max()
    min_profit = df["Profit"].min()

    col1, col2,col3,col4= st.columns(4)

    col1.metric("Total Profit", f"{total_profit:,.2f}")
    col2.metric("Average Profit", f"{avg_profit:,.2f}")
    col3.metric("Maximum Profit", f"{max_profit:,.2f}")
    col4.metric("Minimum Profit", f"{min_profit:,.2f}")

    if "Category" in df.columns:
        profit_category = df.groupby("Category", as_index=False)["Profit"].sum()

        fig_profit = px.bar(
            profit_category,
            x="Category",
            y="Profit",
            text_auto=True,
            title="Profit by Category"
        )

        st.plotly_chart(fig_profit, use_container_width=True)


if "Year Month" in df.columns and "Profit" in df.columns:
    monthly_profit = df.groupby("Year Month", as_index=False)["Profit"].sum()

    fig1 = px.line(
        monthly_profit,
        x="Year Month",
        y="Profit",
        markers=True,
        title="Monthly Profit Trend"
    )

    st.plotly_chart(fig1, use_container_width=True)



st.subheader("Yearly Profit Trend")

if "Year" in df.columns and "Profit" in df.columns:
    yearly_profit = df.groupby("Year", as_index=False)["Profit"].sum()

    fig2 = px.bar(
        yearly_profit,
        x="Year",
        y="Profit",
        text_auto=True,
        title="Yearly Profit Trend"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Month Wise Profit Comparison")

if "Month" in df.columns and "Month Number" in df.columns and "Profit" in df.columns:
    month_profit = df.groupby(
        ["Month Number", "Month"],
        as_index=False
    )["Profit"].sum()

    month_profit = month_profit.sort_values("Month Number")

    fig3 = px.bar(
        month_profit,
        x="Month",
        y="Profit",
        text_auto=True,
        title="Month Wise Profit Comparison"
    )

    st.plotly_chart(fig3, use_container_width=True)
