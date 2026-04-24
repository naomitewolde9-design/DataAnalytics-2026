USE northwind;

-- 1) Write a query to list the product id, product name, and unit price of every product.
-- This time, display them in ascending order by price.

SELECT ProductID, ProductName, UnitPrice
FROM products
ORDER BY UnitPrice ASC; 

-- 2) What are the products that we carry where we have at least 100 units on hand? 
-- Order them in descending (DESC) order by price.
-- Sirop d'rable, Grandma's Boysenberry Spread, Pt chinois, Gustaf's Knckebrd, Inlagd Sill,
-- Boston Crab Meat, Rd Kaviar, Sasquatch Ale, Rhnbru Klosterbier, Geitost. 

SELECT ProductName, UnitsInStock, UnitPrice
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;

-- 3) What are the products that we carry where we have 'at least 100' (=>) units on hand? Order
-- them in descending order by price. If two or more have the same price, list those in
-- ascending order by product name.
-- Sirop d'rable
-- Grandma's Boysenberry Spread
-- Pt chinois
-- Gustaf's Knckebrd
-- Inlagd Sill
-- Boston Crab Meat
-- Rd Kaviar
-- Sasquatch Ale
-- Rhnbru Klosterbier
-- Geitost
SELECT ProductName, UnitsInStock, UnitPrice
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASC;

-- 4) Write a query against the orders table that displays the total number of distinct
-- customers who have placed orders, based on customer ID. Use an alias to label the
-- count calculation as CustomerCount.
-- QUERY: 
SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders;  

-- 5) Write a query against the orders table that displays the total number of distinct
-- customers who have placed orders, by customer ID, for each country where orders
-- have been shipped. Again, use an alias to label the count as CustomerCount. Order
-- the list by the CustomerCount, largest to smallest.

-- NOTES: Using DESC because we need largest to smallest. Using COUNT to count the number of rows 
-- putting the column customer ID counts all the rows from that column "CustomerID" and with DISTINCT it
-- counts each customer only once per country, even if they placed multiple orders.
-- GROUP BY takes all rows that have the same ShipCountry value and treat them as one group. 
-- Instead of multiple rows it would jus be groups. 
SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount
FROM orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;

-- 6) What are the products that we carry where we have less than 25 units on hand, but 1
-- or more units of them are on order? Write a query that orders them by quantity on
-- order (high to low), then by product name. 

-- Louisiana Hot Spiced Okra, Wimmers gute Semmelkndel, Aniseed Syrup, Chocolade, Gorgonzola Telino, Rogede sild, Maxilaku,
-- Gravad lax, Chang, Mascarpone Fabioli, Sir Rodney's Scones, Queso Cabrales, Longlife Tofu, Gnocchi di nonna Alice, 
-- Ipoh Coffee, Outback Lager, Scottish Longbreads. 

SELECT ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock < 25 
AND UnitsOnOrder >= 1
ORDER BY UnitsOnOrder DESC, 
ProductName ASC;

-- 7) Write a query to list each of the job titles in employees, along with a count of how
-- many employees hold each job title.

SELECT Title, 
Count(EmployeeID) 
AS EmployeeCount
FROM employees
GROUP BY Title;

-- 8) What employees have a monthly salary that is between $2000 and $2500? Write 
-- query that orders them by job title. 
-- Laura	Callahan
-- Michael	Suyama
-- Anne	Dodsworth
-- Andrew	Fuller
SELECT FirstName, LastName, Title, Salary
FROM employees
WHERE Salary 
BETWEEN 2000 AND 2500
ORDER BY Title ASC;