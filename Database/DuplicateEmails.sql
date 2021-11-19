------------------------------------------------------------------------------------------------
182. Duplicate Emails
------------------------------------------------------------------------------------------------
Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.


---------------------------------------------------------------------------------------------------------
Solution
---------------------------------------------------------------------------------------------------------

create table Person ( id int(11), email varchar(100));

Test Case 1

INSERT INTO `Person` (`id`,`email`)VALUES(1,'a@b.com');
INSERT INTO `Person` (`id`,`email`)VALUES(2,'c@d.com');
INSERT INTO `Person` (`id`,`email`)VALUES(3,'a@b.com');

Test Case 2

INSERT INTO `Person` (`id`,`email`)VALUES(2,'paris@hilton.com');
INSERT INTO `Person` (`id`,`email`)VALUES(3,'mickey@disney.com');


select Email from Person group by email having count(email) > 1

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
