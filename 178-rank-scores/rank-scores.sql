# Write your MySQL query statement below
select score,
Dense_rank() over (order by score desc) as 'rank'
from Scores order by score  desc;