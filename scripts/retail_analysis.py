# --- IMPORTS (Crucial to prevent 'pd not defined' errors) ---
import pandas as pd  #
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# --- STEP 1: DATA PRE-PROCESSING ---
# Ensure 'retail_sales_data.csv' is in the same folder
df = pd.read_csv('retail_sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Handle missing values
df.fillna(df.median(numeric_only=True), inplace=True)

# Feature Engineering with correct column names
# Use 'Price per Unit' as specified in tasks
df['Total_Amount'] = df['Quantity'] * df['Price per Unit']
df['Month'] = df['Date'].dt.month
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 18, 25, 35, 50, 100], labels=['<18', '18-25', '26-35', '36-50', '50+'])

# --- STEP 2: PREDICTIVE ANALYTICS ---
# Customer Segmentation (K-Means)
X_clusters = df[['Age', 'Total_Amount']]
kmeans = KMeans(n_clusters=3, n_init=10).fit(X_clusters)
df['Customer_Segment'] = kmeans.labels_

# Sales Forecasting (Random Forest)
X = df[['Month', 'Quantity']]
y = df['Total_Amount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestRegressor().fit(X_train, y_train)

# Export for Step 3: Dashboarding
df.to_csv('cleaned_retail_data.csv', index=False)

print("Project Analysis Complete. 'cleaned_retail_data.csv' is ready.")