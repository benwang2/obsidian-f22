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
CREATE PROCEDURE API1(
	IN c VARCHAR(6),
    IN ts Timestamp,
    IN p VARCHAR(50)
)
BEGIN
	IF (c NOT IN ('Biden','Trump')) THEN
		SIGNAL SQLSTATE '45000' 
			SET MESSAGE_TEXT = 'Invalid candidate';
	END IF;
    
    IF (p NOT IN (SELECT DISTINCT precinct FROM Penna)) THEN
		SIGNAL SQLSTATE '45000' 
			SET MESSAGE_TEXT = 'Invalid precinct';
	END IF;

	SELECT
		CASE
			WHEN c='Biden' THEN Biden
            WHEN c='Trump' THEN Trump
            ELSE -1
		END AS Votes
        FROM Penna
        WHERE precinct=p AND Timestamp <= ts
        ORDER BY Timestamp DESC
        LIMIT 1;
END$$
DELIMITER ;
```
### API2(date)
Given a date, return the candidate who had the most votes at the last timestamp for this date as well as  how many votes he got. For example the last timestamp for 2020-11-06 will be 2020-11-06 23:51:43.

```mysql
DROP PROCEDURE IF EXISTS API2;
DELIMITER $$
CREATE PROCEDURE API2(
	IN d DATE
)
BEGIN
	IF (d NOT REGEXP '[0-9]{4}-[0-9]{2}-[0-9]{2}') THEN
		SIGNAL SQLSTATE '45000' 
			SET MESSAGE_TEXT = 'Invalid date format: Must be YYYY-MM-DD';
	END IF;

	SELECT IF(Biden>Trump, "Biden", "Trump") AS winningCandidate
    FROM Penna
    WHERE Timestamp LIKE CONCAT(d," %")
    ORDER BY Timestamp DESC
    LIMIT 1;
END$$
DELIMITER ;
```

### API3(candidate)
Given a candidate return top 10 precincts that this candidate won. Order precincts by total votes and list TOP 10 in descending order of totalvotes.

```mysql
DROP PROCEDURE IF EXISTS API3;
DELIMITER $$
CREATE PROCEDURE API3(
	IN candidate VARCHAR(6)
)
BEGIN
	IF (c NOT IN ('Biden','Trump')) THEN
		SIGNAL SQLSTATE '45000' 
			SET MESSAGE_TEXT = 'Invalid candidate';
	END IF;

	SELECT p.precinct
	FROM (
		SELECT DISTINCT precinct
		FROM Penna
		WHERE 1 = CASE
				WHEN candidate='Biden' THEN Biden>Trump
				WHEN candidate='Trump' THEN Trump>Biden
				ELSE -1
			END
	) p
	ORDER BY (
		SELECT MAX(totalvotes) FROM Penna WHERE precinct=p.precinct
	) DESC
	LIMIT 10;
END$$
DELIMITER ;
```

### API4(precinct)
Given a precinct, show who won this precinct (Trump or Biden) as well as what percentage of total votes went to the winner.

```mysql
DROP PROCEDURE IF EXISTS API4;
DELIMITER $$
CREATE PROCEDURE API4(
	IN p VARCHAR(64)
)
BEGIN
	IF (p NOT IN (SELECT DISTINCT precinct FROM Penna)) THEN
		SIGNAL SQLSTATE '45000' 
			SET MESSAGE_TEXT = 'Invalid precinct';
	END IF;

	SELECT
		IF(Biden>Trump,'Biden','Trump') as winner,
	CONCAT(FORMAT(IF(
		Biden>Trump,
        Biden/totalVotes,
        Trump/totalVotes
	)*100, 2), "%") as percentage
	FROM (SELECT * FROM Penna WHERE precinct=p) penna
	WHERE penna.Timestamp = (SELECT MAX(Timestamp) FROM penna);
END$$
DELIMITER ;
```

## API5(string)
Given a string $s$ of characters, create a stored procedure which determines who won more votes in all precincts whose names contain this string s and how many votes did they get in total. For example, for s='Township', the procedure will return the name (Trump or Biden) who won more votes in union of precints which have "Township" in their name as well as the sum of votes for the winner.
```mysql
DROP PROCEDURE IF EXISTS API5;
DELIMITER $$
CREATE PROCEDURE API5(
	IN s VARCHAR(64)
)
BEGIN
	SELECT
		IF(Biden>Trump,'Biden','Trump') as winner,
		IF(Biden>Trump, SUM(Biden), SUM(Trump)) as votes
	FROM (
		SELECT Timestamp, Trump, Biden
        FROM Penna
        WHERE precinct LIKE CONCAT('%',s,'%')
	) penna
	WHERE penna.Timestamp = (SELECT MAX(Timestamp) FROM penna);
END$$
DELIMITER ;
```

## Part 2 (30%)
### newPenna(precinct, Timestamp, totalVotes, Trump, Biden)
This stored procedure will create a table newPenna, showing for each precinct how many votes were added to totalvotes, Trump, Biden between timestamp T and the las timestamp directly preceding  T.  In other words, create a table like Penna but replace totalvotes with newvotes, Trump with new_Trump and Biden with new_Biden.  Stored procedure with cursor is recommended
```mysql
DROP PROCEDURE IF EXISTS newPenna;
DELIMITER $$
CREATE PROCEDURE newPenna(
	IN p VARCHAR(64),
    IN ts Timestamp,
    IN tv INT,
    IN Trump INT,
    IN Biden INT
)
BEGIN
	DECLARE cur CURSOR FOR (
		SELECT *
        FROM Penna
        WHERE precinct = p AND Timestamp <= ts
        ORDER BY timestamp
        LIMIT 2
	);
    
	DROP TABLE IF EXISTS tempPenna;
	CREATE TEMPORARY TABLE tempPenna (
		precinct VARCHAR(64),
        Timestamp Timestamp,
        newVotes INT,
        newTrump INT,
        newBiden INT
    );
    
	-- INSERT INTO tempPenna( 
	-- 		precinct, Timestamp, newVotes, newTrump, newBiden
	-- 	)
	--     VALUES (
	-- 		p, ts, 
	--     )
END$$
DELIMITER ;
```

### Switch(precinct, timestamp, fromCandidate, toCandidate)
This stored procedure will return list of precincts, which have switched their winner from one candidate in last 24 hours of vote collection (i.e 24 hours before the last Timestamp data was collected) and that candidate was the ultimate winner of this precinct.

## Part 3 (10%)
Write SQL queries or stored procedures to check if the following patterns are enforced in the database:
1. The sum of votes for Trump and Biden cannot be larger than totalvotes
2. There cannot be any tuples with timestamps later than Nov 11 and earlier than Nov3
3. Totalvotes for any precinct and at any timestamp T > 2020-11-05 00:00:00, will be larger or equal to totalvotes at T’<T where T’>2020-11-05 00:00:00 for that precinct.

You should write SQL queries to verify the constraints and return TRUE or FALSE (in case constraint is not satisfied).Queries that don’t return a boolean value won’t be accepted.  

## Part 4 (30%)
### Triggers and UPDATE driven Stored Procedures
Create three tables Updated Tuples, Inserted Tuples and Deleted Tuples. All three tables should have the same schema as Penna and should store any tuples which were updated (store them as they were before the update), any tuples which were inserted,  and any tuples which were deleted in their corresponding tables.  The triggers should populate these tables upon each update/insertion/deletion. There will be one trigger for the update operation, one trigger for the insert operation and one trigger for the delete operation.

### Stored Procedure Simulating Trigger
**MoveVotes(Precinct, Timestamp, Candidate, Number_of_Moved_Votes)**
1. Precinct – one of the existing precinct
2. Timestamp must be existing timestamp. If Timestamp does not appear in Penna than MoveVotes should display a message “Unknown Timestamp”.
3. The Number_of_Moved_Votes  parameter  (always positive integer) shows the number of votes to be moved from the Candidate to another candidate and it cannot be larger  than number of votes that the Candidate has at the Timestamp.  If this is the case MoveVotes () should display a message “Not enough votes”.
4. Of course if CoreCandidate is neither Trump nor Biden, MoveVotes() should say “Wrong Candidate”

After you are done with exceptions, you should move the Number_of_Moved_Votes from CoreCandidate to another candidate (there are only two) and do it not just for this Timestamp (the first parameter) but also for all T>Timestamp, that is all future timestamps in the given precinct. 

For example MoveVotes(Red Hill, 2020-11-06 15:38:36,’Trump’,100) will remove 100 votes from Trump and move it to Biden at 2020-11-06 15:38:36 and all future timestamps after that in the Red Hill precinct.