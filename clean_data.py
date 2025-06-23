import pandas as pd


file_path = "C:/Users/achsa/OneDrive/Desktop/project/data.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')

print(df.info())
print(df.head())

df = df.dropna()  # or use df.fillna() for specific imputations

df = df.drop_duplicates()

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print(df.nunique())

df.to_csv("C:/Users/achsa/OneDrive/Desktop/project/cleaned_data.csv", index=False)
