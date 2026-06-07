import pandas as pd
import plotly.express as px
import streamlit as st

# Page config
st.set_page_config(page_title='Sales Dashboard', layout='wide')

# Load and prepare data
df = pd.read_csv('Data/Superstore_clean.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# App title
st.title('📊 Sales Dashboard')
st.write('Analysis of Superstore Sales Data (2014-2017)')   

# Sidebar Filters
st.sidebar.title('Filters')

regions = st.sidebar.multiselect('Select Region', 
                                  df['Region'].unique(),
                                  default=df['Region'].unique())

categories = st.sidebar.multiselect('Select Category',
                                     df['Category'].unique(),
                                     default=df['Category'].unique())

# Apply filters
df = df[df['Region'].isin(regions)]
df = df[df['Category'].isin(categories)]


# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric('Total Sales', f"${df['Sales'].sum():,.0f}")
col2.metric('Total Profit', f"${df['Profit'].sum():,.0f}")
col3.metric('Total Orders', f"{df['Order ID'].nunique():,}")
col4.metric('Profit Margin', f"{(df['Profit'].sum() / df['Sales'].sum() * 100):.1f}%")

st.divider()

# Sales and Profit by Region
region = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()

fig1 = px.bar(region, x='Region', y=['Sales', 'Profit'], 
              title='Sales and Profit by Region',
              barmode='group')
st.plotly_chart(fig1)

st.caption('💡 Central has higher sales than South but lower profit - suggests heavy discounting or high costs')

st.divider()

# Sales and Profit by Category
category = df.groupby('Category')[['Sales', 'Profit']].sum().reset_index()

fig2 = px.bar(category, x='Category', y=['Sales', 'Profit'],
              title='Sales and Profit by Category',
              barmode='group')
st.plotly_chart(fig2)

st.caption('💡 Furniture has high sales but very low profit - Tables and Bookcases are loss makers')

st.divider()

# Sales and Profit by Sub-Category
subcategory = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().reset_index()
subcategory = subcategory.sort_values('Sales', ascending=False)

fig3 = px.bar(subcategory, x='Sub-Category', y=['Sales', 'Profit'],
              title='Sales and Profit by Sub-Category',
              barmode='group')
st.plotly_chart(fig3)

st.caption('💡 Tables and Bookcases have negative profit - they are loss makers dragging down Furniture category')

st.divider()

# Sales Trend over Time
monthly_sales = df.groupby(['Order Year', 'Order Month'])['Sales'].sum().reset_index()
monthly_sales['Date'] = pd.to_datetime({'year': monthly_sales['Order Year'], 
                                         'month': monthly_sales['Order Month'], 
                                         'day': 1})
fig4 = px.line(monthly_sales, x='Date', y='Sales',
               title='Monthly Sales Trend (2014-2017)')
st.plotly_chart(fig4)

st.caption('💡 Sales growing year over year with consistent spikes in Sep, Nov and Dec every year')

st.divider()

# Sales and Profit by Segment
segment = df.groupby('Segment')[['Sales', 'Profit']].sum().reset_index()

fig5 = px.bar(segment, x='Segment', y=['Sales', 'Profit'],
              title='Sales and Profit by Customer Segment',
              barmode='group')
st.plotly_chart(fig5)

st.caption('💡 Consumer segment drives majority of sales and profit - most valuable customer group')

