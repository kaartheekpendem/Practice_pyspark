-- Rank employees globally and within each department by salary.
select *,rank() over(partition by department order by salary desc) as r from employees_details