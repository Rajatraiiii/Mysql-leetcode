# Write your MySQL query statement below
select e.name,d.bonus from Employee e left join Bonus d
on e.empId=d.empId where d.bonus<1000 OR bonus is null;