------------------------------------------------------------------------------------------------
181. Employees Earning More Than Their ManagersEmployees Earning More Than Their Managers
------------------------------------------------------------------------------------------------
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |  --> Manager
| 4  | Max   | 90000  | NULL      |  --> Manager
+----+-------+--------+-----------+

Given the Employee table, write a SQL query that finds out employees who earn more than their managers. 
For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+

---------------------------------------------------------------------------------------------------------
Solution
---------------------------------------------------------------------------------------------------------

create table Employee (
				id 			int(11),
				name 		varchar(100),
				salary 		int(11),
				ManagerId 	int(11)
);


INSERT INTO `employee` (`id`,`name`,`salary`,`ManagerId`)VALUES(1,'Joe',70000,3);
INSERT INTO `employee` (`id`,`name`,`salary`,`ManagerId`)VALUES(2,'Henry',80000,4);
INSERT INTO `employee` (`id`,`name`,`salary`,`ManagerId`)VALUES(3,'Sam',60000,null);
INSERT INTO `employee` (`id`,`name`,`salary`,`ManagerId`)VALUES(4,'Max',90000,null);



Algorithm

As this table has the employee's manager information, we probably need to select information from it twice.

SELECT *
FROM Employee AS a, Employee AS b
;
Note: The keyword 'AS' is optional.

Id	Name	Salary	ManagerId	Id	Name	Salary	ManagerId
1	Joe		70000	3			1	Joe		70000	3
2	Henry	80000	4			1	Joe		70000	3
3	Sam		60000				1	Joe		70000	3
4	Max		90000				1	Joe		70000	3

1	Joe		70000	3			2	Henry	80000	4
2	Henry	80000	4			2	Henry	80000	4
3	Sam		60000				2	Henry	80000	4
4	Max		90000				2	Henry	80000	4

1	Joe		70000	3			3	Sam		60000	
2	Henry	80000	4			3	Sam		60000	
3	Sam		60000				3	Sam		60000	
4	Max		90000				3	Sam		60000	

1	Joe		70000	3			4	Max		90000	
2	Henry	80000	4			4	Max		90000	
3	Sam		60000				4	Max		90000	
4	Max		90000				4	Max		90000	


The first 3 columns are from a and the last 3 ones are from b.

Select from two tables will get the Cartesian product of these two tables. In this case, the output will be 4*4 = 16 records. 
However, what we interest is the employee's salary higher than his/her manager. So we should add two conditions in a WHERE clause like below.

SELECT
    *
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id
        AND a.Salary > b.Salary
;

Id	Name	Salary	ManagerId	Id	Name	Salary	ManagerId
1	Joe		70000	3			3	Sam		60000	



SELECT emp.name employee 
  FROM employee emp,employee mgr
 WHERE emp.managerid = mgr.id
   AND emp.salary > mgr.salary
   
+----------+
| Employee |
+----------+
| Joe      |
+----------+
   
   