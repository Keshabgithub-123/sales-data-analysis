import pandas as pd

# Load data
df = pd.read_csv('../data/sales_data.csv')

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

# Remove missing values
df = df.dropna()

# Create new column
df['Revenue_per_unit'] = df['Sales'] / df['Quantity']

# Save cleaned data
df.to_csv('../data/cleaned_sales_data.csv', index=False)

print("✅ Data cleaned and saved!")