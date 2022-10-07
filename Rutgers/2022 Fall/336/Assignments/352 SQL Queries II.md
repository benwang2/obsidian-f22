---
title: 352 SQL Queries II
course: CS_336
released: 2022/10/04
due: 2022/10/10
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
    AND f.drinker='Gunjan'
    AND f.bar=s.bar;
```

	# bar


### 3. Drinkers who frequent only bars which serve all beers they like

### 4. Drinkers who frequent most popular bar (the one with highest count of drinkers)

### 5. Precinct(s) which collected the least number of  total votes by end of day of November 5th 2020

### 6. Which precincts did Trump win by more than 100 votes in 2020

### 7. Has Trump ever led the total vote (for any of the timestamps)?  (Return "Yes he did on \<timestamp>" or "No he never did".