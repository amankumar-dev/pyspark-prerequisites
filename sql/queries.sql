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

