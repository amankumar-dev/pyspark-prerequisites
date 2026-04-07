-- 1) What is GROUP BY? (select total number order done by each customer)
SELECT 
	count(orderid) num_of_order,
	custid
	FROM order_table
	group by custid
	order by num_of_order

-- 2) What is HAVING? (select those customer who order more than 30 times)
select 
    o.custid,
    count(*) as total_orders
    from order_table o
    group by o.custid
    having count(*) > 30
    order by total_orders;

-- 3) What is window function? (select total number order done by each customer)
SELECT 
	custid,
	count(*) over(partition by custid) num_of_order
	FROM order_table
	order by num_of_order

-- 4) What is ROW_NUMBER() (select total number order done by each customer and assign a row number for each)?
SELECT 
	custid,
	count(*) over(partition by custid) as num_of_order,
	row_number(*) over(partition by custid) as rn
	FROM order_table

-- 5) What is RANK()? (rank the customer on the basis of number of orders they placed)
SELECT *,
       RANK() OVER (ORDER BY num_of_order DESC)
FROM (
    SELECT custid,
	COUNT(*) as num_of_order
    FROM order_table
    GROUP BY custid
) t;

-- 6) What is partition by?
-- Partition by wo hai jo ek condition pr partition kr deta hai aur operation perform krta hai pr row collapse nhi krta group by ke trah

-- 7) What is Indexing?
CREATE INDEX idx_custid 
ON order_table(custid);

-- 8) What is normalization?
-- Normalization is the process of structuring a relational database to minimize redundancy and improve data integrity using normal forms like 1NF, 2NF, and 3NF.

-- 9) What is star schema?
-- Star schema is a data warehouse schema where a central fact table is connected to multiple denormalized dimension tables in a star-like structure.

-- 10) What is ETL?
-- Process of extracting data and transform into optimized form of data and then load into the database.