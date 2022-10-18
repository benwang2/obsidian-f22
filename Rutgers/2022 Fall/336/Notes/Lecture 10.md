---
title: Lecture Notes 10
course: CS_336
date: 2022-10-14
tags: 
- lectureNotes
- CS_336
---

<center><h1>Lecture 10</h1></center>

## Topics Covered
- keys
- REFERENCES keyword
- FOREIGN KEY
- CHECK
- ASSERTION
- TRIGGERS


## Keys
A key is a minimal subset of attributes which uniquely determine the whole tuple. One of these subsets is selected as a primary key. A primary key does not allow NULLs.

The key is declared in the CREATE TABLE statement,

Key constraints can be violated.
e.g. key is beer, and two bars sell the same beer at different princes

A constraint that requires a beer to in Sells be a beer in Beers is called a **foreign key**.

A foreign key is to be shared by a relation R and a relation S.

Any attributes referenced by forein keys must be declared as PRIMRY KEY or UNIQUE

### Foreign-Key Constraints
Two violations are possible
- an insert or update to R introduces values not found in S
- a deletion or update to S causes some tuple of R to "dangle"

Actions taken for violation
- reject
- delete tuple
- set null

FOREIGN KEY(beer)
	REFERENCES Beers(name)
	ON DELETE SET NULL
	ON UPDATE CASCADE

## Policies
...

## Assertions
We must check every assertion after each modification to the database