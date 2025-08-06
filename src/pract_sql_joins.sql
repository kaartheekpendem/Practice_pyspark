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