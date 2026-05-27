import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def read_csv(file):
    df=pd.DataFrame(file)
    return df
df=pd.read_excel('data/sales.xls')
print(df.shape)
st.title('Sales Data Analysis')
st.write('Shape of data: ',df.shape)

# st.dataframe(df.head())


