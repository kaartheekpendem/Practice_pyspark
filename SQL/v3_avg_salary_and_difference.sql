-- For each department, compute the salary difference between each employee and the department average.
--1
with cte as(
select id, first_name, last_name, age, department, role, salary, dt_update, avg(salary) over(partition by department) as avg_salary from employees_details
)
select id, first_name, last_name, age, department, role, salary, dt_update,cast (salary - avg_salary as decimal(22,3)) as  av_salary from cte
--2
select a.id, a.first_name, a.last_name, a.age, a.department, a.role, a.dt_update,cast(a.salary-b.avg_sal as decimal(25,2)) as av_sal from employees_details a
left join (select department,avg(salary) as avg_sal from employees_Details
group by department) b
on a.department =b.department
