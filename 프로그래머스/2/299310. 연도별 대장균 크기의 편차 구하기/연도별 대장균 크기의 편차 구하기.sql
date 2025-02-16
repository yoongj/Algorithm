-- 코드를 작성해주세요
select year(differentiation_date) as YEAR,
(select max(size_of_colony)
      from ecoli_data sub
      where year(main.differentiation_date) = year(sub.differentiation_date)) - main.size_of_colony as YEAR_DEV, ID
from ecoli_data main

order by year(differentiation_date) asc, year_dev asc;