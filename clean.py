import pandas as pd
df = pd.read_csv('Data/Superstore.csv', encoding='latin-1')

#fix date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

#extract year, month, day from order date
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Day'] = df['Order Date'].dt.day

#remove duplicates
df.drop_duplicates(inplace=True)

#check if everything is correct
print(df.dtypes)
print(df.shape)
df.to_csv('Data/Superstore_clean.csv', index=False)

# Sales by Region
#region_sales = df.groupby('Region')['Sales'].sum().reset_index()
#region_sales = region_sales.sort_values('Sales', ascending=False)

#fig1 = px.bar(region_sales, x='Region', y='Sales', title='Sales by Region')
#st.plotly_chart(fig1)

#st.caption('💡 West region leads in sales, followed by East, Central and South')

# Profit by Region
#region_profit = df.groupby('Region')['Profit'].sum().reset_index()
#region_profit = region_profit.sort_values('Profit', ascending=False)

#fig2 = px.bar(region_profit, x='Region', y='Profit', title='Profit by Region')
#st.plotly_chart(fig2)

#st.caption('💡 Central has higher sales than South but lower profit - suggests heavy discounting or high costs')
#this is from app.py for my understanding, I have removed it from app.py and added it here in clean.py to avoid confusion and make the code cleaner.