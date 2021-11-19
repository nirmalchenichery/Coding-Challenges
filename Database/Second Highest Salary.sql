-------------------------------------------------------------------------------------------------------
176. Second Highest Salary
-------------------------------------------------------------------------------------------------------

Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the query should return 200 as the second highest salary. 
If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

-------------------------------------------------------------------------------------------------------
Solution
-------------------------------------------------------------------------------------------------------

CREATE TABLE `employee` (
						  `id` int(11) DEFAULT NULL,
						  `name` varchar(100) DEFAULT NULL,
						  `salary` int(11) DEFAULT NULL,
						  `ManagerId` int(11) DEFAULT NULL
): 



INSERT INTO `employee` (`id`, `name`, `salary`, `ManagerId`) VALUES
(1, 'Joe', 70000, 3),
(2, 'Henry', 80000, 4),
(3, 'Sam', 60000, NULL),
(4, 'Max', 90000, NULL);



select max(salary) as SecondHighestSalary
from employee
where (salary) < (select max(salary) from employee)