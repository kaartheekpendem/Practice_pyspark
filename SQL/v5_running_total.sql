-- For each employee, compute the running total of salary ordered by dt_update.

select *,sum(salary) over(order by id, dt_update rows between unbounded preceding and current row ) as dt from (select distinct * from employees_Details)

