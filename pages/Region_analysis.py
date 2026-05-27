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
st.subheader("Region Analysis")

if "Region" in df.columns:
  
    region_summary = df.groupby("Region", as_index=False).agg({"Sales": "sum","Profit": "sum","Quantity": "sum"})

    col1,col2,col3 = st.columns(3)

    col1.metric("Total Regions", region_summary.shape[0])
    col2.metric("Highest Sales Region", region_summary.loc[region_summary['Sales'].idxmax(), 'Region'])
    col3.metric("Highest Profit Region", region_summary.loc[region_summary['Profit'].idxmax(), 'Region'])
    fig_region_sales = px.bar(
        region_summary,
        x="Region",
        y="Sales",
        text_auto=True,
        title="Region Wise Sales"
    )

    st.plotly_chart(fig_region_sales, use_container_width=True)

    st.subheader("Region Table")
    st.dataframe(region_summary, use_container_width=True)
