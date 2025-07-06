# Retail Sales Analysis with SQL & Python (Superstore Dataset)

This is a beginner-friendly **Data Engineering & SQL Analytics** project that focuses on designing a simple relational data model, extracting insights with SQL, and visualizing key business metrics using Python.

---

## Dataset

- Source: [Superstore Dataset on Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- Raw data was provided as a single CSV file and later normalized into 3 separate tables with Seperation.ipynb:
  - `customers.csv`
  - `products.csv`
  - `orders.csv`

---

## Project Objectives

1. Normalize raw sales data into a relational database (PostgreSQL)
2. Build tables using SQL with appropriate keys and constraints
3. Analyze key business questions using SQL queries
4. Visualize insights using Python (Pandas, Matplotlib)
5. Structure and document the project professionally on GitHub

---

## Tools & Technologies

- **SQL** (PostgreSQL)
- **Python** (Pandas, Matplotlib)
- **Jupyter Notebook**
- **Kaggle Dataset**
- **Git/GitHub**

---

## Data Model (Schema)

```sql
customers(customer_id [PK], customer_name, segment, city, state, country)
products(product_id [PK], product_name, category, sub_category, price)
orders(order_id [PK], order_date, ship_date, customer_id [FK], product_id [FK], quantity, sales, profit)
See schema.sql

---

## Key Questions Answered with SQL

- SQL queries are in analysis.sql
    1. What are the total sales and profits? What is our profit margin?

    2. Have monthly sales trends been growing?

    3. When did we have the highest monthly sales?

    4. Which product categories bring the most revenue and profit?

    5. Which states are most profitable?

    6. Are there products with high sales but low profit margins?

    7. How long does it take to ship orders, by category?

---

## Visualizations & Analysis

See analysis.ipynb

Sample charts include:

    - Line plot of monthly sales trend

    - Bar chart of sales & profit by category

    - Horizontal bar chart of average shipping delays by category

    - Scatter plot: High sales, low profit products

    - Horizontal bar chart of profit by state

All charts are saved in the plots/ folder

---

## Folder Structure

Superstore-Analysis/
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
|   └── Sample_Superstore.csv
├── notebook/
│   ├── analysis.ipynb
│   └── seperation.ipynb
├── sql/
│   ├── schema.sql
│   └── analysis.sql
├── plots/
│   └── (charts)
├── requirements.txt
└── README.md

---

## Requirements

Install the necessary Python packages:
    ```bash pip install -r requirements.txt```

---

## Author

Parsa Kamali Shahry
Data Engineer | Python & SQL Enthusiast
LinkedIn https://www.linkedin.com/in/parsa-kamali-243934305/

---

## Next Steps

    Convert this analysis into a pipeline (ETL-style)

    Load results into a dashboard (Power BI / Tableau / Streamlit)

    Move data to a cloud DB (e.g. Google BigQuery, AWS RDS)