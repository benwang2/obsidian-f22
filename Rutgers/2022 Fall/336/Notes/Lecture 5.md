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
	- Natural joins and outer joins
	- Left join, right join
- Conditionals
	- Case statements
	- If function

## Joins
### Natural join
A **natural join** joins two tables based on same attribute name and data types. The table that results from this operation contains all the attributes of both tables, but keeps only one copy of each common column.

#### Example
**Students**
| id  | name |
| --- | ---- |
| 1   | john |
| 2   | sam  |
| 3   | meg  |

**Grades**
| id  | grade |
| --- | ---- |
| 1   | 50 |
| 2   | 75  |
| 3   | 99  |

Suppose we run the following query:
```sql
SELECT *
FROM Students NATURAL JOIN Grades;
```

We would get the output:
| id  | name | grade |
| --- | ---- | ----- |
|     |      |       |