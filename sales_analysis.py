import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv")

# Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

# Add month column
df['Month'] = df['Date'].dt.month

# Revenue calculation
df['Revenue'] = df['Quantity'] * df['Price']

# EDA - Monthly Sales
monthly_sales = df.groupby('Month')['Revenue'].sum()

plt.figure()
monthly_sales.plot(kind='bar')
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# Top products
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(5)
print("Top Products:\n", top_products)