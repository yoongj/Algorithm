-- 코드를 작성해주세요
select route, concat(ROUND(SUM(D_BETWEEN_DIST),1),'km') as TOTAL_DISTANCE, concat(ROUND(avg(d_between_dist),2),'km') AS AVERAGE_DISTANCE
from subway_distance

group by route

ORDER BY ROUND(SUM(D_BETWEEN_DIST),1) DESC;