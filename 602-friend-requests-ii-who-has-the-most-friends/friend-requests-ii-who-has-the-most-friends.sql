select id, COUNT(*) AS num
from (select requester_id AS id from RequestAccepted
    UNION ALL
select accepter_id AS id from RequestAccepted
) AS all_friends group by id order by num DESC limit 1;
