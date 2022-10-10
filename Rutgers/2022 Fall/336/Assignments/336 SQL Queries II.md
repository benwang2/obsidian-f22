---
title: 352 SQL Queries II
course: CS_336
released: 2022-10-04
due: 2022-10-10
tags: 
- Assignments
- CS_336
---
<center><h1>SQL Queries II</h1></center>
<center><h3>CS 210 - Principles of Information and Data Management</h3></center>

### 1. Drinkers who like the most beers (highest number of beers)
```sql
SELECT DISTINCT drinker
FROM Likes
GROUP BY drinker
HAVING count(*)=(SELECT count(*) as c1 FROM Likes
	GROUP BY drinker
    ORDER BY c1 DESC
    LIMIT 1
```

	# drinker
	'Mike'

### 2. Bars which sell most expensive Budweiser and are not frequented by Gunjan
```sql
SELECT DISTINCT s.bar
FROM 
	Sells s,
    Frequents f,
    (SELECT MAX(price) as MaxPrice FROM Sells WHERE beer='Budweiser') as mp
WHERE
	s.beer='Budweiser'
    AND s.price=mp.MaxPrice
    AND f.drinker!='Gunjan'
    AND f.bar=s.bar;
```

	# bar
	'Caravan'


### 3. Drinkers who frequent only bars which serve all beers they like

### 4. Drinkers who frequent most popular bar (the one with highest count of drinkers)

```sql
SELECT DISTINCT f.drinker
FROM
	Frequents f,
    (
		SELECT bar, count(*) as num_drinkers 
        FROM Frequents 
        GROUP BY bar 
        ORDER BY count(*) DESC
        LIMIT 1
	) AS c
WHERE f.bar = c.bar;
```

	# drinker
	'Bob'
	'Erik'
	'Herb'
	'Jesse'
	'Joe'
	'John'
	'Justin'
	'Mike'
	'Rebecca'
	'Tom'
	'Vince'
	'Jeanie'
	'Tatiana'
	'Yuhan'

### 5. Precinct(s) which collected the least number of  total votes by end of day of November 5th 2020
```sql
SELECT DISTINCT p1.precinct
FROM Penna p1
WHERE p1.Timestamp LIKE '2020-11-05 %'
GROUP BY precinct
HAVING MAX(p1.totalvotes)=(
    SELECT MAX(totalvotes) as t2
	From Penna as p
	WHERE p.Timestamp LIKE '2020-11-05 %'
	GROUP BY p.precinct
	ORDER BY t2 ASC
	LIMIT 1
);
```

	# precinct
	'Franconia 2'


### 6. Which precincts did Trump win by more than 100 votes in 2020
```sql
SELECT 
    DISTINCT IF(SUM(Trump) - SUM(Biden) > 100,
        precinct,
        0) Result
FROM
    Penna
GROUP BY precinct
HAVING Result != 0
```

	# Result
	'043 W BRANDYWINE W'
	'060 W CALN 1'
	'061 W CALN 2'
	'165 E COVENTRY 2'
	'215 ELK'
	'220 ELVERSON'
	'235 W FALLOWFIELD'
	'290 HIGHLAND'
	'295 HONEY BROOK BORO'
	'300 HONEYBROOK TWP 1'
	'301 HONEYBROOK TWP 2'
	'335 LONDONDERRY'
	'380 W NANTMEAL'
	'405 EAST NOTTINGHAM EAST'
	'406 EAST NOTTINGHAM WEST'
	'410 W NOTTINGHAM'
	'430 LOWER OXFORD W'
	'435 UPPER OXFORD'
	'545 W SADSBURY'
	'705 WARWICK W'
	'26-01'
	'26-02'
	'26-03'
	'26-04'
	'26-05'
	'26-06'
	'26-07'
	'26-09'
	'39-36'
	'39-41'
	'45-01'
	'45-03'
	'45-04'
	'45-05'
	'45-20'
	'45-23'
	'45-25'
	'57-13'
	'57-14'
	'57-17'
	'58-04'
	'58-21'
	'58-33'
	'58-35'
	'58-39'
	'58-41'
	'63-03'
	'63-17'
	'65-01'
	'65-02'
	'65-07'
	'66-06'
	'66-09'
	'66-14'
	'66-29'
	'66-34'
	'66-36'
	'66-43'
	'66-45'


### 7. Has Trump ever led the total vote (for any of the timestamps)?  (Return "Yes he did on \<timestamp>" or "No he never did".
```sql
SELECT 
	CONCAT(
		IF(Trump>Biden, "Yes he did on ","No he never did"),
		IF(Trump>Biden, Timestamp, "")
	)
FROM Penna1
LIMIT 1;
```
	# CONCAT(
			IF(Trump>Biden, "Yes he did on ","No he never did"),
			IF(Trump>Biden, Timestamp, "")
		)
	'Yes he did on 2020-11-04 03:58:36'