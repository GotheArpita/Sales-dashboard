import pandas as pd

df = pd.read_csv("Data/Superstore.csv", encoding="latin-1")

print("Shape: ", df.shape)

print("\nColumns: ", df.columns)

print("\nData Types: ", df.dtypes)

print("\nMissing Values: ", df.isnull().sum())

print("\nFirst 5 Rows: \n", df.head())
