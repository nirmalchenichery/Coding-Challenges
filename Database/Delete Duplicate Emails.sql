--------------------------------------------------------------------------------------------------
196. Delete Duplicate Emails
--------------------------------------------------------------------------------------------------

Write a SQL query to delete all duplicate email entries in a table named Person, 
keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+

Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

Note:

Your output is the whole Person table after executing your sql. Use delete statement.

--------------------------------------------------------------------------------------------------
Solution
--------------------------------------------------------------------------------------------------

Create table Person ( id int(11), email varchar(100));

INSERT INTO `Person` (`id`,`email`)VALUES(1,'john@example.com');
INSERT INTO `Person` (`id`,`email`)VALUES(2,'bob@example.com');
INSERT INTO `Person` (`id`,`email`)VALUES(3,'john@example.com');




Get all of the duplicate e-mail addresses:

SELECT 
    EMAILADDRESS, COUNT(1)
FROM
    TABLE
GROUP BY EMAILADDRESS
HAVING COUNT(1) > 1
Then determine the ID from that gives:

SELECT
    ID
FROM 
    TABLE
WHERE 
    EMAILADDRESS IN (
        SELECT 
            EMAILADDRESS
        FROM
            TABLE
        GROUP BY EMAILADDRESS
        HAVING COUNT(1) > 1
    )
Then finally, delete the rows, based on the above and other constraints:

DELETE 
FROM 
    TABLE
WHERE
    ID IN (
        SELECT
            ID
        FROM 
            TABLE
        WHERE 
            EMAILADDRESS IN (
                SELECT 
                    EMAILADDRESS
                FROM
                    TABLE
                GROUP BY EMAILADDRESS
                HAVING COUNT(1) > 1
            )
    )  
    AND FIRSTNAME = 'Instant'
	
	
	