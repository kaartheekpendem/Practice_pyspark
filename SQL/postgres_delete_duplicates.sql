with cte as (
select * ,row_number() over(partition by id order by id)  r,ctid from public.incremental1
)
delete from public.incremental1 i
using cte c
where i.id = c.id
and i.ctid>c.ctid
