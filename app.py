
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Vehicle Data Analysis')

duplicate_rows = df.duplicated().sum()

df = df.drop_duplicates()

median_cylinder = df.groupby(['model', 'model_year'])['cylinders'].transform('median')

df['cylinders'].fillna(median_cylinder, inplace=True)

st.subheader('Odometer Distribution by Model Year')
histogram = px.histogram(df, x='model_year', y='odometer', labels={'model_year': 'Model Year'})
st.plotly_chart(histogram)


min_year = int(df['model_year'].min())
max_year = int(df['model_year'].max())
selected_year = st.slider('Select model year for filter', min_value=min_year, max_value=max_year, value=(min_year, max_year))

filtered_df = df[(df['model_year'] >= selected_year[0]) & (df['model_year'] <= selected_year[1])]

st.subheader(f'Price Distribution by Vehicle Type (Model Year: {selected_year[0]} - {selected_year[1]})')
histogram2 = px.histogram(filtered_df, x='type', y='price', title=f'Price Distribution by Vehicle Type (Model Year: {selected_year[0]} - {selected_year[1]})')
st.plotly_chart(histogram2)

st.subheader('Scatter Plot: Model Year vs. Price')
scatter_plot = px.scatter(filtered_df, x='model_year', y='price', title=f'Model Year vs Price (Model Year: {selected_year[0]} - {selected_year[1]})', labels={'model_year': 'Model Year'})
st.plotly_chart(scatter_plot)


if st.checkbox('Exclude very expensive vehicles (price > 50,000)'):
    filtered_df = df[df['price'] <= 50000]
    scatter_plot_filtered = px.scatter(filtered_df, x='model_year', y='price', title='Model Year vs Price (Filtered: Price ≤ 50,000)', labels={'model_year': 'Model Year'})
    st.plotly_chart(scatter_plot_filtered)
