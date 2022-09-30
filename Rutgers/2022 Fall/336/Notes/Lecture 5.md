---
title: Lecture Notes 5
course: CS_336
date: 2022-09-27
tags: 
- Lecture Notes
- CS_336
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

## Example tables
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


## Joins
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
#natural_join

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
#inner_join

### Outer join
Outer joins return all specified records when there's a match in the tables specified. It effectively **unions** two tables on the basis specified in the **ON** clause.

#### Full outer join
A full outer join will combine both tables completely.

Suppose we run the following query on the example tables.
```sql
SELECT S.id, S.name, G.grade
FROM Students S
FULL OUTER JOIN Grades G ON S.id=G.id
```

We would get the output
| id  | name | grade |
| --- | ---- | ----- |
| 1   | john | NULL  |
| 2   | sam  | 50    |
| 3   | meg  | 75    |
| 4   | NULL | 99      |
#full_outer_join

#### Left join
A LEFT JOIN joins two tables and returns all records from the left table, and the matching records from the right table. In the event there are no matches in the right side, there will be 0 rows with columns from the right table.
#left_join

#### Right join
A RIGHT JOIN joins two tables and returns all records from the right table, and the matching records from the left table. In the event there are no matches in the left side, there will be 0 rows with columns from the left table.
#right_join

## Conditionals
### Case statement
The CASE expression goes through conditions and returns a value when the first condition is met, similarly to an if-then-else statement. Once a condition is true, it will stop reading and return the result. If no conditions are true, it returns the value in the ELSE clause.

Suppose we run the query:
```sql
SELECT s.id, s.name, s.grade
	CASE
		WHEN s.grade > 90 THEN "A"
		WHEN s.grade > 80 THEN "B"
		WHEN s.grade > 70 THEN "C"
		WHEN s.grade > 60 THEN "D"
		ELSE "F"
	END AS grade_letter
FROM Students s
LEFT JOIN Grades g
WHERE s.id = g.id
```

We would get the output:
| id  | name | grade | letter |
| --- | ---- | ----- | ------ |
| 2   | sam  | 50    | F      |
| 3   | meg  | 75    | C      |
#case

### If-then statement
The IF function takes 3 parameters and looks like this.
```sql
IF(condition, value_if_true, value_if_false)
```

The parameters are as following:
| Parameter        | Description                                         |
| ---------------- | --------------------------------------------------- |
| *condition*      | The value / expression to evaluate to true or false |
| *value_if_true*  | The value to return if *condition* is **true**.     |
| *value_if_false* | The value to return if *condition* is **false**.    |

To extend the use of the IF function, we can use the **STRCMP** function. This lets us test whether two strings are the same.

For example,
```sql
SELECT IF(STRCMP("hello","bye") = 0, "YES", "NO");
```

Furthermore, we can use the IF function to add an additional column to our returned records.

For example:
```sql
SELECT s.id, s.name, IF(g.grade>=60, "PASSING", "FAILING")
FROM Students s
LEFT JOIN Grades g ON s.id = g.id
```
would return the following:
| id  | name | IF(g.grade>=60, "PASSING", "FAILING") |
| --- | ---- | ------------------------------------- |
| 2   | sam  | FAILING                               |
| 3   | meg  | PASSING                               |

#if_then