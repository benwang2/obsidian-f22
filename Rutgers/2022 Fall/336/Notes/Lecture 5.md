---
title: Lecture Notes 5
course: CS_336
date: 2022-09-27
tags: "Lecture Notes"
---

# Lecture 5
Imielinski doesn't really have a structure to his lectures, so notes here are from recording topics he covers and doing research on my own.

## Topics Covered
- Joins
	- Natural joins, inner joins, and outer joins
	- Left join, right join
- Conditionals
	- Case statements
	- If function

## Joins
### Example tables
**Students**
| id  | name |
| --- | ---- |
| 1   | john |
| 2   | sam  |
| 3   | meg  |

**Grades**
| id  | grade |
| --- | ---- |
| 2   | 50 |
| 3   | 75  |
| 4   | 99  |


### Natural join
A **natural join** joins two tables based on same attribute name and data types. The table that results from this operation contains all the attributes of both tables, but keeps only one copy of each common column.

Suppose we run the following query:
```sql
SELECT *
FROM Students NATURAL JOIN Grades;
```

We would get the output:
| id  | name | grade |
| --- | ---- | ----- |
| 2   | sam  | 50    |
| 3   | meg  | 75      |

The natural join requires that similar rows occur in both tables, and only then will it join the row in **Grades** to the row in **Students**.

### Inner join
An **inner join** joins two tables using the condition specified in the **ON** clause. The resulting table contains all attributes from both tables, including common columns.

Suppose we run the following query on the example tables.
```sql
SELECT *
FROM Students S
INNER JOIN Grades G ON S.id = G.id;
```

We would get the output:
| id  | name | id  | grade |
| --- | ---- | --- | ----- |
| 2   | sam  | 2   | 50    |
| 3   | meg  | 2   | 75

