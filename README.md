# 📊 Sales Data Analysis & Dashboard

## 🔍 Overview
This project analyzes retail sales data to uncover key business insights and visualize performance using Python, SQL, and Power BI.

The goal is to help businesses track sales trends, identify top-performing products, and understand regional performance for better decision-making.

---

## 📌 Business Problem
Organizations need to monitor sales performance across regions and categories to:
- Identify high-revenue products
- Track monthly sales trends
- Analyze regional performance
- Improve business strategies using data-driven insights

---

## 📊 Dataset
- Source: Superstore Dataset
- Type: Retail sales data
- Key Features:
  - Order Date, Ship Date
  - Category, Sub-Category
  - Region
  - Sales
  - Profit *(simulated for analysis purposes)*

---

## 🛠️ Tools & Technologies
- Python (Pandas, NumPy)
- SQL (SQLite)
- Power BI
- Jupyter Notebook
- VS Code

---

## ⚙️ Project Workflow
1. Data Collection & Loading
2. Data Cleaning & Preprocessing (Python)
3. Feature Engineering (Profit, Profit Margin)
4. Exploratory Data Analysis (EDA)
5. SQL-based Analysis
6. Dashboard Creation (Power BI)

---

## 📊 Dashboard Preview
![Dashboard](dashboard/Sales_Data_Analysis_Dashboard.png)

---

## 📈 Key Insights
- Technology category contributes the highest share of total sales
- West region generates maximum revenue compared to other regions
- Sales show clear monthly trends with seasonal spikes
- Certain sub-categories significantly outperform others in revenue generation
- Profit margins vary across categories indicating optimization opportunities



▶️ How to Run the Project

Install dependencies:

pip install pandas numpy jupyter

Run data cleaning script:

python scripts/data_cleaning.py

Open Jupyter Notebook:

notebooks/analysis.ipynb

Open Power BI dashboard:

dashboard/sales_dashboard.pbix

---

## 🗄️ SQL Analysis (Sample Queries)
```sql
-- Sales by Category
SELECT Category, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Category;

-- Region-wise Sales
SELECT Region, SUM(Sales) AS Revenue
FROM sales
GROUP BY Region;

-- Monthly Sales Trend
SELECT strftime('%Y-%m', "Order Date") AS Month, SUM(Sales)
FROM sales
GROUP BY Month
ORDER BY Month;



