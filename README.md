# 📦 E-commerce Return Rate Reduction Analysis

This project analyzes product return patterns in an e-commerce dataset using Python, SQL, and Power BI. It focuses on identifying why customers return products and how return rates vary by category, geography, and marketing channels. A predictive model is developed to estimate return risk and an interactive dashboard is created for business insights.

---

## 📌 Objective

- Understand key drivers of product returns
- Analyze return behavior across categories and countries
- Predict high-risk return products using machine learning
- Visualize return trends and risk scores in Power BI

---

## 🛠️ Tools & Technologies

- **Python**: Data cleaning, transformation, and model building  
- **SQL (MySQL)**: Data aggregation and filtering  
- **Scikit-learn**: Logistic regression model for predicting return risk  
- **Power BI**: Interactive dashboard with drill-through analytics  
- **Pandas, NumPy**: Data manipulation  
- **SQLAlchemy**: Database connection

---

## 📂 Project Structure

Ecommerce_Return_Analysis/
│
├── code/
│ ├── clean_data.py # Cleans raw CSV data
│ └── data import.py # Imports data, trains ML model, exports predictions
│
├── data/
│ ├── data.sql 
│ ├── online_dataset.csv 
│ ├── cleaned_data.csv 
│ ├── cleanest_data.csv 
│ └── high_risk_products.csv 
│
├── dashboard/
│ └── main.pbix 
│
├── report/
│ ├── Ecommerce_Return_Analysis_Report.docx 
│ └── project final..pdf 


## 📊 Key Metrics

| Metric               | Value      |
|----------------------|------------|
| Total Orders         | ~8,000     |
| Total Returns        | 402        |
| Return Rate          | ~5%        |
| High-Risk Products   | Exported if return risk > 60% |

---

## 🧠 Machine Learning Model

- **Model**: Logistic Regression
- **Target Variable**: `return_flag` (1 = return, 0 = no return)
- **Features**: `unitprice`, `quantity`, `category` (one-hot encoded)
- **Train/Test Split**: 80/20 with stratification
- **Output**: Return probability for each product

---

## 📈 Power BI Dashboard

Includes:

- Return Rate by Product Category
- Total Returns by Country
- Time-based Return Trends (Year, Quarter, Month, Day)
- Return Risk Score Drill-Down
- Interactive Filters and Tooltips

---

## 📤 Output

> **`high_risk_products.csv`** contains products with return probability > 60%, allowing business teams to take corrective action (e.g., improving descriptions, packaging, or supplier checks).
