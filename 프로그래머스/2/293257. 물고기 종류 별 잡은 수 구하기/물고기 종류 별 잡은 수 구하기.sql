-- 코드를 작성해주세요
select count(*) AS FISH_COUNT, fn.fish_name as FISH_NAME
from fish_info fi join fish_name_info fn on fi.fish_type=fn.fish_type

group by fi.fish_type, fn.fish_name

order by fish_count desc;
