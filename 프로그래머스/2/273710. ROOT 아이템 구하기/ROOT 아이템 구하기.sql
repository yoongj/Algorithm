-- 코드를 작성해주세요
select ii.item_id as ITEM_ID, ii.item_name as ITEM_NAME
from item_info ii join item_tree it on ii.item_id=it.item_id

where it.parent_item_id is null

order by ITEM_ID;