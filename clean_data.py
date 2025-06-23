import pandas as pd

# Load the dataset
file_path = "C:/Users/achsa/OneDrive/Desktop/project/data.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# View basic info
print(df.info())
print(df.head())

# Handle missing values
df = df.dropna()  # or use df.fillna() for specific imputations

# Remove duplicates
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Check unique values
print(df.nunique())

# Save cleaned data
df.to_csv("C:/Users/achsa/OneDrive/Desktop/project/cleaned_data.csv", index=False)
