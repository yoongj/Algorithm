-- 코드를 작성해주세요
SELECT fi.ID, fn.FISH_NAME, fi.LENGTH
from fish_info fi join fish_name_info fn on fi.fish_type=fn.fish_type

where fi.length = (select max(length)
       from fish_info
       where fi.fish_type = fish_info.fish_type
      )

order by fi.ID asc;


# select max(length)
#        from fish_info
#        group by fish_info.fish_type