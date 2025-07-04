CREATE TABLE customers (
"customer_id" VARCHAR(8) PRIMARY KEY,
"customer_name" TEXT,
"segment" TEXT,
"city" TEXT,
"state" TEXT,
"country" TEXT
);
CREATE TABLE products (
"product_id" VARCHAR(15) PRIMARY KEY,
"product_name" TEXT,
"category" TEXT,
"sub_category" TEXT,
"price" FLOAT
);
CREATE TABLE orders (
"order_id" VARCHAR(14) PRIMARY KEY,
"order_date" DATE,
"ship_date" DATE,
"customer_id" VARCHAR(8) REFERENCES customers("customer_id"),
"product_id" VARCHAR(15) REFERENCES products("product_id"),
"quantity" INT CHECK("quantity" > 0),
"sales" FLOAT,
"profit" FLOAT
);