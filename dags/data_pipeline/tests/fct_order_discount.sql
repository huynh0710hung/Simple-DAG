-- Singularity test
--Check if any item_discount has negative value
select 
	*
from 
	{{ref('fct_orders')}}
where item_discount_amount >0