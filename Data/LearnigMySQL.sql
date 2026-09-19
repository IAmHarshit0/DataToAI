select * from demo.computersales;
select Sex, Age, `Product Type`, Contact, `Lead`, `Month`, `Year`, Profit from  demo.computersales;
select * from demo.computersales where Sex = "M" and `Product Type` = "Laptop";
select * from demo.computersales where Sex = "M" or `Product Type` = "Laptop";
select * from demo.computersales where Contact like "%mar%";
select * from demo.computersales order by `Product Type` asc, Age desc;
select * from demo.computersales  limit 2,3;
select * from demo.computersales where Age between 30 and 40;
select * from demo.computersales where `Product Type` not in ("Laptop", "Tablet");
select concat(`Product ID`,"-", `Product Type`) as Product from demo.computersales;
select concat_ws(" - ", `Product ID`, `Product Type`) as Product from demo.computersales;
select length(Contact) as Count from demo.computersales;
select Upper(Contact) from demo.computersales;
select lower(Contact) from demo.computersales;
select left(Contact, 4) from demo.computersales;
select right(Contact, 4) from demo.computersales;
select mid(Contact, 2,5) from demo.computersales;
select sum(Profit) as total from demo.computersales;
select count(Contact) from demo.computersales;
select avg(`Sale Price`) from demo.computersales;
select max(Profit) from demo.computersales;
select min(Profit) from demo.computersales;
select truncate(Profit, 0) as Profit from demo.computersales;
select ceil(Profit) as upper from demo.computersales;
select floor(Profit) as lower from demo.computersales;
# select date(``) as from 
# select datediff() as from 
# select time() as from 
# select dayname() as from 
# select monthname() as from 
# select year() as from 
# select minute() as from 
# selcett hour() as from ;
select Age, `Sale Price`, Profit, 
case
	when Profit < 500 then "Less than 500"
    else "Greater than or equal to 500"
end as New_Profit 
from demo.computersales;
select * from demo.computersales;
SELECT 
    `Product Type`, COUNT(`Product ID`)
FROM
    demo.computersales
GROUP BY `Product Type`
HAVING COUNT(`Product ID`) > 5;
-- select products.productName, orderdetails.quantityOrdered from products 
-- inner join orderdetails 
-- on products.productCode = orderdetails.productCode 
-- group by products.productName;

-- select products.productName, orderdetails.quantityOrdered 
-- from products left/right join orderdetails
-- on products.productCode = orderdetails.productCode 

-- select * from products cross join orderdetails
-- on products.productCode = orderdetails.productCode 

-- select FirstName, Department from employee2
-- union 
-- select FirstName, Department from employee1;

-- select FirstName, Department from employee2
-- union all
-- select FirstName, Department from employee1;

-- select FirstName, Department from employee2
-- intersect
-- select FirstName, Department from employee1;

-- select FirstName, Department from employee2
-- where FirstName in (select FirstName from employee1)

-- select FirstName, Department from employee2
-- except
-- select FirstName, Department from employee1;

-- select FirstName, Department from employee2
-- where FirstName not in (select FirstName from employee1)

-- select * from classicmodels.customers where creditLimit > 
-- (select avg(creditLimit) from classicmodels.customers); 

-- create view `` as 

-- Delimiter && 
-- create procedure get_data(in var int)
-- begin 
-- 	select * from demo.computersales limit var;
-- end &&
-- Delimiter ;
-- call demo.get_data(3)

-- Delimiter && 
-- create procedure get_data(out var int)
-- begin 
-- 	select * from demo.computersales into var;
-- end &&
-- Delimiter ;
-- call demo.get_data(@``)

-- Delimiter && 
-- create procedure get_data(inout var int)
-- begin 
-- 	select customerName from customers where customerNumber = var;
-- end &&
-- Delimiter ;
-- call classicmodels.get_data(@``)
-- select @``

-- select FirstName, Occupation, EducationLevel, TotalChildren, sum(TotalChildren) 
-- over(partition by Occupation order by EducationLevel) from customers_data;