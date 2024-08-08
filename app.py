
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Vehicle Data Analysis')

histogram = px.histogram(df, x='model_year', y='odometer')
st.plotly_chart(histogram)

histogram2 = px.histogram(df, x='type', y='price')
st.plotly_chart(histogram2)

scatter_plot = px.scatter(df, x='model_year', y='price')
st.plotly_chart(scatter_plot)

if st.checkbox('Show scatter plot'):
    st.plotly_chart(scatter_plot)
