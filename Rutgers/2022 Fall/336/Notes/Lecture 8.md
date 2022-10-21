---
title: Lecture Notes 8
course: CS_336
date: 2022-10-07
tags: 
- lectureNotes
- CS_336
---

<center><h1>Lecture 8</h1></center>

## Topics Covered
- update/insert/delete
- stored procedure
- triggers

## Modifying records in an existing table
### UPDATE
The `UPDATE` command isused to modify existing rows in a table. It follows the syntax of
```sql
UPDATE tableName
SET columnName = 'newValue', column2Name = 'newValue2'
WHERE columName = 'valueToMatch';
```

You can combine N number of conditions using the AND or the OR operators.

### INSERT
The `INSERT` command is used to add new rows of data to a table in the database. The command is used with the following syntax:
```SQL
INSERT INTO tableName (column1, column2, column3)
VALUES (value1, value2, value3)
```

Using the select statement, you can populate one table using another table. For example, we could write
```SQL
INSERT INTO destinationTable []
```

## DELETE keyword
...

## Stored Procedures
...

## Triggers
.