import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 1. Database connection settings
DB_USER = 'root'                # <-- change if needed
DB_PASS = 'Achsah,2005'       # <-- change this to your actual MySQL password
DB_NAME = 'data'       # <-- change to your MySQL database name
DB_HOST = 'localhost'
DB_PORT = '3306'
TABLE_NAME = 'cleaned_data'

# 2. Create SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# 3. Load data from SQL
df = pd.read_sql(f"SELECT * FROM cleaned_data", engine)
df.columns = df.columns.str.strip().str.lower()  # Normalize column names

# 4. Clean data
df.dropna(subset=['customerid', 'description'], inplace=True)
df['invoicedate'] = pd.to_datetime(df['invoicedate'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unitprice'] = pd.to_numeric(df['unitprice'], errors='coerce')

# 5. Create return_flag column
df['return_flag'] = df['quantity'].apply(lambda x: 1 if x < 0 else 0)

# 6. Simulate returns if only one class is found
if df['return_flag'].nunique() < 2:
    print("⚠️ No real returns found — forcing simulation.")
    sim_indices = df.sample(frac=0.05, random_state=42).index
    df.loc[sim_indices, 'quantity'] = -1
    df['return_flag'] = df['quantity'].apply(lambda x: 1 if x < 0 else 0)

print("✅ Return flag distribution:\n", df['return_flag'].value_counts())

# 7. Create a 'category' column based on first word of description (very basic)
df['category'] = df['description'].str.extract(r'(\b[A-Z]+\b)', expand=False).fillna('UNKNOWN')

# 8. Prepare features and target
X = pd.get_dummies(df[['unitprice', 'quantity', 'category']], drop_first=True)
y = df['return_flag']

# 9. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# 10. Model training
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 11. Evaluation
y_pred = model.predict(X_test)
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# 12. Predict return probability for all
df['return_risk_score'] = model.predict_proba(X)[:, 1]

# 13. Export high-risk products
high_risk = df[df['return_risk_score'] > 0.6]
high_risk.to_csv("high_risk_products.csv", index=False)
print(f"✅ Exported {len(high_risk)} high-risk products to high_risk_products.csv")

# 14. (Optional) Save cleaned full dataset
df.to_csv("cleanest_data.csv", index=False)


