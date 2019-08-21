-- Write a query in PostgresSQL syntax to get names of the youngest customers.
-- Save your query as an .sql file.

-- find 5 names of youngest customers
select name from customers order by dob desc limit 1;
