USE northwind;

-- 1) Write a query to find the price of the cheapest item that Northwind sells. Then write a
-- second query to find the name of the product that has that price.

-- Geitost	2.5000

SELECT MIN(UnitPrice)
AS CheapestPrice
FROM products;

SELECT ProductName, UnitPrice
FROM products

WHERE UnitPrice = 
(SELECT MIN(UnitPrice)
FROM products);

-- 2) Write a query to find the average price of all items that Northwind sells.
-- (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
-- using the ROUND function to round the average price to the nearest cent.)

-- 28.87

SELECT AVG(UnitPrice) 
AS AveragePrice
FROM products;

SELECT ROUND(AVG(UnitPrice), 2) 
AS AveragePrice
FROM products;

-- 3) Write a query to find the price of the most expensive item that Northwind sells. Then
-- write a second query to find the name of the product with that price, plus the name of
-- the supplier for that product.

-- Cte de Blaye,	263.5000,	Aux joyeux ecclsiastiques

SELECT MAX(UnitPrice) 
AS ExpensivePrice
FROM products;

SELECT
p.ProductName,
p.UnitPrice,
s.CompanyName 
AS SupplierName
FROM products AS p
INNER JOIN suppliers AS s
	ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (SELECT MAX(UnitPrice) 
FROM products);

-- 4) Write a query to find total monthly payroll (the sum of all the employees’ monthly
-- salaries).

-- 20362.929931640625

SELECT SUM(Salary) 
AS TotalMonthlyPayroll
FROM employees;

-- 20362.93

SELECT ROUND(SUM(Salary), 2)
AS TotalMonthlyPayroll
FROM employees;

-- 5) Write a query to identify the highest salary and the lowest salary amounts which any
-- employee makes. (Just the amounts, not the specific employees!)
-- HIGHEST SALARY: 3119.15	LOWEST SALARY: 1744.21

SELECT MAX(Salary) AS HighestSalary,
MIN(Salary) AS LowestSalary
FROM employees;

-- 6) Write a query to find the name and supplier ID of each supplier and the number of
-- items they supply. Hint: Join is your friend here.

SELECT s.CompanyName AS SupplierName,
		s.SupplierID, COUNT(p.ProductID)
        AS NumberOfSuppliedItems
        
FROM suppliers AS s
LEFT JOIN products AS p
ON s.SupplierID = p.SupplierID

GROUP BY s.CompanyName, s.SupplierID
ORDER BY s.CompanyName;

-- 7) Write a query to find the list of all category names and the average price for items in
-- each category.

SELECT c.CategoryName,
 ROUND(AVG(p.UnitPrice), 2)
		AS AveragePrice
        
FROM categories AS c
INNER JOIN products AS p
ON c.CategoryID = p.CategoryID

GROUP BY c.CategoryName
ORDER BY c.CategoryName;

-- 8) Write a query to find, for all suppliers that provide at least 5 items to Northwind, 
-- what is the name of each supplier and the number of items they supply.

-- Pavlova, Ltd., SUPPLIER ID: 7, NUMBER OF ITEMS: 5
-- Plutzer Lebensmittelgromrkte AG, SUPPLIER ID: 12, NUMBER OF ITEMS: 5

SELECT s.CompanyName AS SupplierName,
		s.SupplierID, COUNT(p.ProductID)
        AS NumberOfSuppliedItems
        
FROM suppliers AS s
INNER JOIN products AS p
ON s.SupplierID = p.SupplierID

GROUP BY s.CompanyName, s.SupplierID
HAVING COUNT(p.ProductID) >= 5

ORDER BY NumberOfSuppliedItems DESC;

-- 9) Write a query to list products currently in inventory by the product id, product name,
-- and inventory value (calculated by multiplying unit price by the number of units on
-- hand). Sort the results in descending order by value. If two or more have the same
-- value, order by product name. If a product is not in stock, leave it off the list.

SELECT ProductID, ProductName,
	(UnitPrice*UnitsInStock)
	AS InventoryValue
        
FROM products
WHERE UnitsInStock>0
ORDER BY InventoryValue DESC,
		ProductName ASC;