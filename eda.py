import pandas as pd

df = pd.read_csv('Data/Superstore.csv', encoding='latin-1')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Month Name'] = df['Order Date'].dt.strftime('%b')
df.drop_duplicates(inplace=True)

region_sales =df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales)

region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print(region_profit)

# Central has higher sales than South but lower profit
# Suggests heavy discounting or high costs in Central region
category = df.groupby('Category')[['Sales', 'Profit']].sum().sort_values('Profit', ascending=False)
print(category)

# Furniture has high sales but very low profit
# Could be due to heavy discounts or high shipping costs
# Worth investigating at sub-category level

subcategory = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values('Profit', ascending=False)
print(subcategory)

# Tables and Bookcases are loss making sub-categories
# Tables alone loses 17K despite 206K in sales
# These are dragging down the entire Furniture category profit

monthly_sales = df.groupby(['Order Year', 'Order Month'])['Sales'].sum()
print(monthly_sales)

# Sales show consistent growth from 2014 to 2017
# Strong seasonality - Sep, Nov, Dec are peak months every year
# Jan, Feb are consistently the slowest months

segment = df.groupby('Segment')[['Sales', 'Profit']].sum().sort_values('Profit', ascending=False)
print(segment)
pd.set_option('display.float_format', '{:.2f}'.format)
print(segment)

# Consumer segment is the largest - drives 50%+ of total sales
# All 3 segments are proportionally healthy on profit
# No red flags here unlike Furniture category