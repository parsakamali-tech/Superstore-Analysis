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
See sql/schema.sql


 Key Business Questions (SQL)

 SQL Queries are written in sql/analysis.sql

    What are the total sales and profits? What is our profit margin?

    Have monthly sales trends been growing?

    When did we have the highest monthly sales?

    Which product categories generate the most revenue and profit?

    Which states are the most profitable?

    Are there products with high sales but low profit margins?

    How long does it take to ship orders, by category?

 Visualizations & Analysis

 View in notebook/analysis.ipynb

Sample charts include:

     Line chart: Monthly sales trend

     Grouped bar chart: Sales & profit by category

     Horizontal bar chart: Average shipping delay by category

     Scatter plot: High-sales, low-margin products

     Bar chart: Profit by state

All output images are saved in the plots/ folder.

Folder Structure

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

Requirements

To install the required packages:

pip install -r requirements.txt

Author

Parsa Kamali Shahry
Beginner Data Engineer | Python & SQL Enthusiast
LinkedIn https://www.linkedin.com/in/parsa-kamali-243934305/

Next Steps

    Convert this analysis into a pipeline (ETL-style)

    Load results into a dashboard (Power BI / Tableau / Streamlit)

    Move data to a cloud DB (e.g. Google BigQuery, AWS RDS)