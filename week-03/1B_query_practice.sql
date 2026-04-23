USE northwind;

-- 1) Write a query to list the product id, product name, and unit price of every product that
-- Northwind sells. (Hint: To help set up your query, look at the schema preview to see
-- what column names belong to each table. Or use SELECT * to query all columns
-- first, then refine your query to just the columns you want.) 

SELECT ProductID, ProductName, UnitPrice 
FROM products;

-- 2) Write a query to identify the products where the unit price is $7.50 or less.
-- Konbu, Guaran Fantstica, Geitost, Filo mix, Tourtire
-- QUERY:

SELECT UnitPrice, ProductName
FROM products
WHERE UnitPrice <= 7.50; 

-- 3) What are the products that we carry where we have no units on hand, but 1 or more
-- units are on backorder? Write a query that answers this question.
-- Gorgonzola Telino
-- QUERY:

SELECT UnitsInStock, UnitsOnOrder, ProductName 
FROM products 
WHERE UnitsInStock = 0
	AND UnitsOnOrder > 0; 

-- 4) Examine the products table. How does it identify the type (category) of each item
-- sold? Where can you find a list of all categories? Write a set of queries to answer these
-- questions, ending with a query that creates a list of all the seafood items we carry.
--
-- QUERY: 

SELECT CategoryID, CategoryName FROM categories;
SELECT ProductID, ProductName CategoryID FROM products;

SELECT pro.ProductID, pro.ProductName, cat.CategoryName 
FROM products pro
INNER JOIN categories cat 
	 ON pro.CategoryID = cat.CategoryID;
     
-- Selecting the columns *used the table information under schemas to use as a little cheat sheet :) *
-- from left table 'products' and pulling from categories BASED 'ON' CategoryID. 

SELECT pro.ProductID, pro.ProductName, cat.CategoryName, pro.UnitPrice
FROM products pro 
INNER JOIN categories cat
	ON pro.CategoryID = cat.CategoryID
WHERE cat.CategoryName = "Seafood";

-- 5) Examine the products table again. How do you know what supplier each product
-- comes from? Where can you find info on suppliers? Write a set of queries to find the
-- specific identifier for "Tokyo Traders" and then find all products from that supplier.
-- QUERY:
SELECT ProductID, ProductName, SupplierID
FROM Products;

SELECT SupplierID, CompanyName
FROM Suppliers
WHERE CompanyName = 'Tokyo Traders';

SELECT p.ProductID, p.ProductName, s.CompanyName
FROM Products p
INNER JOIN Suppliers s
    ON p.SupplierID = s.SupplierID
WHERE s.CompanyName = 'Tokyo Traders';

-- 6) Examine the products table again. How do you know what supplier each product
-- comes from? Where can you find info on suppliers? Write a set of queries to find the
-- specific identifier for "Tokyo Traders" and then find all products from that supplier.

-- Each product has a supplier shown through a "SupplierID" which supplierID 
-- is found both in the products table and the suppliers table. (CONTEXT)
SELECT ProductID, ProductName, SupplierID
FROM Products;

-- need to find the SupplierID for Tokyo Traders, using where function 
-- can filter through columns. (CONTEXT) SELECT-column, FROM-table, WHERE-column-=-specific column.
-- to find the specific column '=' name). 
SELECT SupplierID
FROM Suppliers
WHERE CompanyName = 'Tokyo Traders';

-- Find all products supplied by Tokyo Traders. You don't have to use AS cmd to create a acronym for your table,
-- it's simplier for me to read it this way. INNER JOIN pulling the similar columns from both tables
SELECT p.ProductID, p.ProductName, s.CompanyName
FROM Products p
INNER JOIN Suppliers s
    ON p.SupplierID = s.SupplierID
WHERE s.CompanyName = 'Tokyo Traders';

-- 6) How many employees work at northwind? What employees have "manager"
-- somewhere in their job title? Write queries to answer each question.
-- STEVEN BUCHANAN
-- QUERY:
-- CONTEXT- COUNT: counts all the rows in employee table, 
SELECT COUNT(*) FROM Employees;

-- CONTEXT: LIKE allows matching and
-- '%()%' means anything before or after so it could be
--  sales manager or regional manager, 
-- or assistant to the regional manager, you get the point naomi stop. either way it
--  will filter through and find anything with manager in the 'title' FROM the employees table

SELECT EmployeeID, FirstName, LastName, Title
FROM Employees
WHERE Title LIKE '%manager%'





