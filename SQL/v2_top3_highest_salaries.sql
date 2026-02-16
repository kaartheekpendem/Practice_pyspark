-- Find the top 3 highest‑paid employees in each department using window functions.
--1
with cte as (
select id, first_name, last_name, age, department, role, salary, dt_update
,row_number() over(partition by id order by salary) as r
from employees_details
)
select id, first_name, last_name, age, department, role, salary, dt_update from cte
where r<3