-- 코드를 입력하세요
SELECT ice.ingredient_type, sum(ship.total_order) as TOTAL_ORDER
from first_half ship join icecream_info ice on ship.flavor=ice.flavor

group by ice.ingredient_type

order by TOTAL_ORDER;