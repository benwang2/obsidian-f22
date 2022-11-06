---
title: Assignment 3 - Penna
course: CS_336
released: YYYY-MM-DD
due: 2022-11-14
tags:
- Assignments
- CS_336
---
<center><h1>Assignment 3 - Penna</h1></center>
<center><h3>CS336</h3></center>

## Part 1 - 30%
**Powering simple interface to Penna table**


### API1(candidate, timestamp, precinct)
Given a candidate C, timestamp T and precinct P, return how many votes did the candidate C have at T or largest timestamp T’ smaller than T, in case T does not appear in Penna.
```mysql
DROP PROCEDURE IF EXISTS API1;
DELIMITER $$
CREATE FUNCTION API1(
	c VARCHAR(6),
    ts Timestamp,
    p VARCHAR(50)
) RETURNS INT DETERMINISTIC
BEGIN
	RETURN (SELECT
		CASE
			WHEN c='Biden' THEN c
            ELSE Trump
		END
        FROM Penna
        WHERE precinct=p AND Timestamp <= ts
        ORDER BY Timestamp DESC
        LIMIT 1
	);
END;$$
```
### API2(date)
Given a date, return the candidate who had the most votes at the last timestamp for this date as well as  how many votes he got. For example the last timestamp for 2020-11-06 will be 2020-11-06 23:51:43.

```mysql
DROP PROCEDURE IF EXISTS API2;
DELIMITER $$
CREATE FUNCTION API2(
	d VARCHAR(10)
) RETURNS VARCHAR(6) DETERMINISTIC
BEGIN
	SELECT IF(Biden>Trump, "Biden", "Trump")
    FROM Penna
    WHERE Timestamp LIKE CONCAT(d," %")
    ORDER BY Timestamp DESC
    LIMIT 1;
END;$$
```