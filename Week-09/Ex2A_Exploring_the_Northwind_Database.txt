### **Ex2A Exploring the Northwind Database**



##### **Categories Table:**



**∗ What does a value in this column represent? What values might you see here?**

The CategoryID represents the products and the categories 



**∗ Is this column a part of the primary key to this table?**

CategoryID



**∗ Is this column a part of a foreign key that points to a record in another table?**

N/A



**∗ Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?**

No, not enough information



**∗ Do you believe this column is appropriately named for Data Analysis purposes?**

Yes



**∗ If not, what might be a more appropriate name?**

N/A



**∗ What might be the data type and format for this column in a Power BI Model?**

Whole Numbers 



**∗ Can you think of any calculations where this column data might be used?**

Counting and grouping categories



##### **Customers Table:**



**∗ What does a value in this column represent? What values might you see here?**

Customer ID column represents each customer through the data 



**∗ Is this column a part of the primary key to this table?**

Yes, it is Customer ID



**∗ Is this column a part of a foreign key that points to a record in another table?**

No



**∗ Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?**

Yes, I think it would be good to include it because it connects to other tables and customers to orders 



**∗ Do you believe this column is appropriately named for Data Analysis purposes?**

Yes and no



**∗ If not, what might be a more appropriate name?**

I would call it Northwind customer info.



**∗ What might be the data type and format for this column in a Power BI Model?**

Text



**∗ Can you think of any calculations where this column data might be used?**

Revenue VS customer or order transactions per customer 



##### **Employees Table:**



**∗ What does a value in this column represent? What values might you see here?**

Employee ID represents employees in the company data



**∗ Is this column a part of the primary key to this table?**

Yes, Employee ID



**∗ Is this column a part of a foreign key that points to a record in another table?**

No



**∗ Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?**

Yes



**∗ Do you believe this column is appropriately named for Data Analysis purposes?**

N/A



**∗ If not, what might be a more appropriate name?**





**∗ What might be the data type and format for this column in a Power BI Model?**

Whole numbers 



**∗ Can you think of any calculations where this column data might be used?**

Orders made by each employee





##### **Employee Territories Table:**



**∗ What does a value in this column represent? What values might you see here?**

Employee ID represents an employee for each territory



**∗ Is this column a part of the primary key to this table?**

Employee ID and Territory ID



**∗ Is this column a part of a foreign key that points to a record in another table?**

Employee ID comes from the Employee table and Territory ID comes from the Territories Table 



**∗ Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?**

Yes because it connects to Employees and Territories 



**∗ Do you believe this column is appropriately named for Data Analysis purposes?**

N/A



**∗ If not, what might be a more appropriate name?**





**∗ What might be the data type and format for this column in a Power BI Model?**

Whole numbers 



**∗ Can you think of any calculations where this column data might be used?**

Employees in each territory, or region because we also have a regions table



##### **Order Details Table:** 



**∗ What does a value in this column represent? What values might you see here?**

OrderID represents each order item



**∗ Is this column a part of the primary key to this table?**

&#x20;Yes, OrderID



**∗ Is this column a part of a foreign key that points to a record in another table?**

Yes, Product ID comes from Products table and Order ID comes from Orders table  



**∗ Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?**

Yes, because it connects orders to products 



**∗ Do you believe this column is appropriately named for Data Analysis purposes?**

Yes



**∗ If not, what might be a more appropriate name?**

N/A



**∗ What might be the data type and format for this column in a Power BI Model?**

Whole numbers 



**∗ Can you think of any calculations where this column data might be used?**

Revenue, amount sold, and total sales



##### **Orders Table:**



**∗ What does a value in this column represent? What values might you see here?**

Order Id from each customer 



**∗ Is this column a part of the primary key to this table?**

Order Id 



**∗ Is this column a part of a foreign key that points to a record in another table?**

Yes, Customer ID from the customer table 



**∗ Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?**

Yes, because it connects Employees, Customers, and Order/Order Details



**∗ Do you believe this column is appropriately named for Data Analysis purposes?**

Yes



**∗ If not, what might be a more appropriate name?**

N/A



**∗ What might be the data type and format for this column in a Power BI Model?**

Whole numbers





**∗ Can you think of any calculations where this column data might be used?**

Order information, number of orders, total orders per customer, and shipping information



##### **Products Table:**



**∗ What does a value in this column represent? What values might you see here?**

Product ID represents each product from company



**∗ Is this column a part of the primary key to this table?**

Yes, ProductID



**∗ Is this column a part of a foreign key that points to a record in another table?**

Yes, Category ID comes from Categories table



**∗ Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?**

Yes, because it connects Products to OrderDetails



**∗ Do you believe this column is appropriately named for Data Analysis purposes?**

Yes



**∗ If not, what might be a more appropriate name?**

N/A



**∗ What might be the data type and format for this column in a Power BI Model?**

Whole numbers



**∗ Can you think of any calculations where this column data might be used?**

Units sold, Total sales per product, and product performance



##### **Region Table:**



**∗ What does a value in this column represent? What values might you see here?**

RegionID represents grouped territories



**∗ Is this column a part of the primary key to this table?**

Yes, RegionID



**∗ Is this column a part of a foreign key that points to a record in another table?**

No



**∗ Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?**

Yes, I think it would help categorizing the territories 



**∗ Do you believe this column is appropriately named for Data Analysis purposes?**

Yes



**∗ If not, what might be a more appropriate name?**

N/A



**∗ What might be the data type and format for this column in a Power BI Model?**

Whole numbers 



**∗ Can you think of any calculations where this column data might be used?**

Number of territories per region and region performance





##### **Shippers Table:**



**∗ What does a value in this column represent? What values might you see here?**

ShipperID reveals shipping company per order



**∗ Is this column a part of the primary key to this table?**

Yes, Shipper ID



**∗ Is this column a part of a foreign key that points to a record in another table?**

No



**∗ Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?**

Yes



**∗ Do you believe this column is appropriately named for Data Analysis purposes?**

Yes



**∗ If not, what might be a more appropriate name?**

N/A



**∗ What might be the data type and format for this column in a Power BI Model?**

Whole numbers 



**∗ Can you think of any calculations where this column data might be used?**

Number of orders per shipper 





##### **Suppliers Table:**



**∗ What does a value in this column represent? What values might you see here?**

Supplier ID represents each company per product



**∗ Is this column a part of the primary key to this table?**

Yes, SupplierID



**∗ Is this column a part of a foreign key that points to a record in another table?**

No



**∗ Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?**

Yes, because it connects Suppliers to Products



**∗ Do you believe this column is appropriately named for Data Analysis purposes?**

Yes



**∗ If not, what might be a more appropriate name?**

N/A



**∗ What might be the data type and format for this column in a Power BI Model?**

Whole numbers 



**∗ Can you think of any calculations where this column data might be used?**

Number of products per supplier





##### **Territories Table:** 



**∗ What does a value in this column represent? What values might you see here?**

Territory ID represents each territory per region



**∗ Is this column a part of the primary key to this table?**

Yes, Territory ID



**∗ Is this column a part of a foreign key that points to a record in another table?**

Yes, Region ID comes from Region table



**∗ Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?**

Yes, because it connects Region to EmployeeTerritories



**∗ Do you believe this column is appropriately named for Data Analysis purposes?**

Yes



**∗ If not, what might be a more appropriate name?**

N/A



**∗ What might be the data type and format for this column in a Power BI Model?**

Whole Numbers 



**∗ Can you think of any calculations where this column data might be used?**

&#x20;Number of employees per territory





