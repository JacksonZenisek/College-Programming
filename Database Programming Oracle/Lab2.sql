-- Lab 2: SQL SELECT

-- In this lab I work on using the SELECT, FROM, WHERE, and ORDER BY to query information from preconfigured database.


-- 1.	Using the BOOKS table, write a query that displays the following information for each book:
•	Book title
•	Category
•	Publication date
•	Retail price
Use column aliases so that the publication date and retail price are displayed with the headings "Publication Date" and "Retail Price." Sort the results alphabetically by book title.

SELECT TITLE,CATEGORY,PUBDATE AS "Publication Date",RETAIL AS "Retail Price"
FROM BOOKS
ORDER BY TITLE;


-- 2.	Using the CUSTOMERS table, write a query that displays the following information for customers who live in Texas:
•	Customer number
•	First name
•	Last name
•	City
•	State
Display the columns in the order listed above.
Sort the results by last name and then by first name.



SELECT CUSTOMER#,LASTNAME,FIRSTNAME,CITY,STATE
FROM CUSTOMERS
WHERE STATE = 'TX'
ORDER BY LASTNAME, FIRSTNAME;


-- 3. 	Using the BOOKS table, write a query that displays all book categories represented in the current inventory. Each category should appear only once in the results. Sort the categories alphabetically.


SELECT DISTINCT CATEGORY
FROM BOOKS
ORDER BY CATEGORY;


-- 4. Using the AUTHOR table, write a query that displays each author's last name and first name together in one column.
Format each author's name as:
Last Name, First Name
There must be a comma followed by a blank space between the last and first names.
Use a column alias so that the combined name is displayed with the heading "Author Name."
Sort the results by the author's last name.


SELECT LNAME || ', ' || FNAME AS "Author Name"
FROM AUTHOR
ORDER By LNAME;


-- 5.	Using the ORDERITEMS table, write a query that displays the following information for each qualifying order item:
•	Order number
•	Item number
•	ISBN
•	Quantity
•	Amount paid for each item
Create a calculated column that determines the item total by multiplying Quantity by Paid Each.
Use a column alias so that the calculated column is displayed with the heading "Item Total."
Include only order items with a quantity greater than 1. Sort the results by order number


SELECT ORDER#,ITEM#,ISBN, QUANTITY,PAIDEACH,QUANTITY*PAIDEACH AS "Item Total"
FROM ORDERITEMS
WHERE QUANTITY > 1
ORDER BY ORDER#;


-- 6.	Using the BOOKS and PUBLISHER tables, write a query that displays the following information for each book:
•	Book title
•	Publisher name
•	Category
Use a column alias so that the publisher name is displayed with the heading "Publisher Name."
Join the tables using the publisher ID. Sort the results by publisher name and then by book title.


-- 7.	Using the ORDERS and CUSTOMERS tables, write a query that displays orders placed by customers who live in Florida.
Display the following columns in the order listed:
•	Order number
•	Order date
•	Customer number
•	First name
•	Last name
Join the tables using the customer number.
Sort the results by order date.


SELECT ORDER#,ORDERDATE,CUSTOMER#,FIRSTNAME,LASTNAME
FROM ORDERS JOIN CUSTOMERS USING(CUSTOMER#)
WHERE SHIPSTATE = 'FL'
ORDER BY ORDERDATE;


-- 8.	Using the ORDERITEMS and BOOKS tables, write a query that displays the following information:
•	Order number
•	Book title
•	Quantity
•	Amount paid for each item
•	Calculated item total
Calculate the item total by multiplying Quantity by Paid Each.
Use a column alias so that the calculated column is displayed with the heading "Item Total."
Include only records with an item total greater than $30.
Sort the results from the highest item total to the lowest.


SELECT ORDER#,TITLE,QUANTITY,PAIDEACH,QUANTITY*PAIDEACH AS "Item Total"
FROM BOOKS NATURAL JOIN ORDERITEMS
WHERE QUANTITY*PAIDEACH > 30
ORDER BY QUANTITY*PAIDEACH DESC;


-- 9.	Using the BOOKS, BOOKAUTHOR, and AUTHOR tables, write a query that displays books in the COMPUTER category and their authors.
Display the following columns in the order listed:
•	Book title
•	Category
•	Author's first name
•	Author's last name
Join the tables using the ISBN and author ID.
Sort the results by book title and then by the author's last name.


SELECT TITLE,CATEGORY,FNAME,LNAME
FROM BOOKS JOIN BOOKAUTHOR USING(ISBN) JOIN AUTHOR USING(AUTHORID)
WHERE CATEGORY = 'COMPUTER'
ORDER BY TITLE,LNAME;



-- 10.	Using the CUSTOMERS, ORDERS, ORDERITEMS, and BOOKS tables, write a query that displays detailed customer, order, and book information.
Display the following columns in the order listed:
•	Customer number
•	Customer first name
•	Customer last name
•	Order number
•	Order date
•	Book title
•	Quantity
•	Amount paid for each item
•	Calculated item total
Calculate the item total by multiplying Quantity by Paid Each.
Use a column alias so that the calculated column is displayed with the heading "Item Total."
Include only books for which Paid Each is greater than $25.
Sort the results by customer last name, order number, and book title.


SELECT CUSTOMER#,FIRSTNAME,LASTNAME,ORDER#,ORDERDATE,TITLE,QUANTITY,PAIDEACH,QUANTITY*PAIDEACH AS "Item Total"
FROM CUSTOMERS NATURAL JOIN ORDERS NATURAL JOIN ORDERITEMS NATURAL JOIN BOOKS
WHERE PAIDEACH > 25
ORDER BY LASTNAME,ORDER#,TITLE;