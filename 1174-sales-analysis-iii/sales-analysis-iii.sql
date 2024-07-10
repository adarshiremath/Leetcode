# Write your MySQL query statement below
select Product.product_id, Product.product_name
from Product
Inner join Sales on Product.product_id = Sales.product_id
GROUP BY Sales.product_id HAVING MIN(Sales.sale_date) >= '2019-01-01'
AND MAX(Sales.sale_date) <= '2019-03-31'