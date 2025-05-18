CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT salary FROM (
      SELECT DISTINCT salary FROM Employee ) AS temp WHERE (SELECT COUNT(DISTINCT salary)
      FROM Employee WHERE salary > temp.salary
    ) = N - 1
    LIMIT 1
  );
END