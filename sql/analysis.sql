--What are the total sales and profits? Which has grown the most? What is our profit margin?
SELECT
	SUM(sales) AS total_sales,
	SUM(profit) AS total_profit,
	SUM(profit) / NULLIF(SUM(sales), 0) AS profit_margin
FROM orders o;
--Have sales trends been growing?
SELECT
	EXTRACT(MONTH FROM order_date) AS month,
	EXTRACT(YEAR FROM order_date) AS year,
	sum(sales) AS monthly_sales
FROM orders
GROUP BY month,year
ORDER BY month;
--When did we have the highest sales?
SELECT
	EXTRACT(MONTH FROM order_date) AS month,
	EXTRACT(YEAR FROM order_date) AS year,
	sum(sales) AS monthly_sales
FROM orders
GROUP BY month,year
ORDER BY monthly_sales DESC
LIMIT 1;
--What product or category has the most sales and profits?
SELECT
	p.category AS category,
	SUM(o.sales) AS sales,
	SUM(o.profit) AS profit,
	ROUND(SUM(o.profit) / NULLIF(SUM(o.sales), 0), 2) AS profit_margin
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY category
ORDER BY profit_margin ASC;
--Which state have the most profit for us?
SELECT
	c.state,
	SUM(o.profit) AS total_profit
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.state
ORDER BY total_profit DESC
LIMIT 1;
--Do we have products that we sell a lot but make little profit from?
SELECT 
    p.product_name,
    sum(o.sales) AS sales,
    sum(o.profit) AS profit,
    sum(o.profit) / NULLIF(SUM(o.sales), 0) AS profit_margin
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
HAVING 
    sum(o.sales) > 1000 --High sales
    AND SUM(o.profit) / NULLIF(SUM(o.sales), 0) < 0.1 --Low profit margin
ORDER BY profit_margin
LIMIT 10;
--How long does it take for orders to be shipped? Are there any delays?
SELECT
	p.category AS category,
	AVG(o.ship_date - o.order_date) AS delay_order
FROM orders o
JOIN products p ON p.product_id = o.product_id
GROUP BY p.category
ORDER BY delay_order DESC;