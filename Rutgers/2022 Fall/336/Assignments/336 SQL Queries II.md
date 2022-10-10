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
)
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
    AND f.bar NOT IN (SELECT DISTINCT bar FROM Frequents WHERE drinker='Gunjan');
```

	# bar
	'Caravan'


### 3. Drinkers who frequent only bars which serve all beers they like
```sql
SELECT DISTINCT l.drinker
FROM Likes l
WHERE l.drinker NOT IN (
	SELECT l1.drinker
	FROM Likes l1 WHERE
		NOT EXISTS (
			SELECT f.drinker
			FROM Frequents f, Sells s
            WHERE
				l.beer = s.beer
				AND f.drinker = l.drinker
                AND f.bar = s.bar
		)
)
```


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
SELECT DISTINCT precinct
FROM
	penna p1,
	(
		SELECT precinct as p, MAX(Timestamp) as t
		FROM penna
		GROUP BY precinct
	) p2
WHERE
	p1.precinct=p2.p
    AND p1.Timestamp = p2.t
    AND trump - biden > 100;
```


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