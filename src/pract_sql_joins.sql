select * from join1;
select * from join2;

--inner join won't retrive nulls
select a.id from join2 a
inner join join1 b on a.id = b.id

select a.id from join2 a
left join join1 b on a.id = b.id

select a.id from join2 a
right join join1 b on a.id = b.id

select a.id from join2 a
cross join join1 b

select * from public.employees
where dt_update > (current_date - interval '2 year')

select extract(day from current_date)
select extract(month from current_date)
select extract(year from current_date)

select *  from public.employees where 360 >
(current_date:: date -dt_update :: date)


select *,ntile(4) over(order by id desc) from public.employees
select *, lead(dt_update) over(order by dt_update desc) from public.employees
select *, lag(dt_update) over(order by dt_update desc) from public.employees



-- Create the table first (if not already created)
CREATE TABLE employees_hierarchy (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  manager_id INT
);

-- Insert hierarchical employee data
INSERT INTO employees_hierarchy (id, name, manager_id) VALUES
(1, 'Alice', NULL),      -- CEO
(2, 'Bob', 1),           -- Reports to Alice
(3, 'Charlie', 1),       -- Reports to Alice
(4, 'David', 2),         -- Reports to Bob
(5, 'Eva', 2),           -- Reports to Bob
(6, 'Frank', 3),         -- Reports to Charlie
(7, 'Grace', 3),         -- Reports to Charlie
(8, 'Henry', 4);         -- Reports to David


select * from employees_hierarchy

WITH RECURSIVE cte AS (
  SELECT id, name, manager_id, 0 AS head
  FROM employees_hierarchy
  WHERE manager_id IS NULL

  UNION ALL

  SELECT e.id, e.name, e.manager_id, a.head + 1 AS head
  FROM cte a
  INNER JOIN employees_hierarchy e ON a.id = e.manager_id
)
SELECT * FROM cte;


select * from incremental
select * from incremental1

merge into incremental as a using
incremental1 as b on a.id = b.id
when matched then
	update set name = b.name
when not matched then
	insert (id,name) values(b.id,b.name)