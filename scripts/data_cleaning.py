import pandas as pd
import numpy as np   # ✅ IMPORTANT (this was missing)

# Load dataset
df = pd.read_csv('../data/superstore.csv', encoding='latin1')

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

# Handle missing values
df = df.dropna()

# Create new features
df['Profit'] = df['Sales'] * np.random.uniform(0.05, 0.3, len(df))
df['Profit Margin'] = df['Profit'] / df['Sales']

# Save cleaned data
df.to_csv('../data/cleaned_superstore.csv', index=False)

print("✅ Superstore data cleaned!")