---
title: Simple SQL Queries
course: CS_336
released: 2022-09-22
due: 2022-10-07
tags: 
- Assignments
- CS_336
---
<center><h1>Simple SQL Queries</h1></center>
<center><h3>CS 210 - Principles of Information and Data Management</h3></center>

Return SQL code as text file plus results which workbench gave you (you can include them in the same txt file). Query + answer. As long as it is readable by a grader, it is fine - text, word, screenshot....but text is easiest.   

### 1.  Find all distinct drinkers whose phone numbers come from area code 917 and who like Budweiser or Bud (synonym!)
```sql
SELECT DISTINCT drinker  
FROM Likes l, Drinkers d  
WHERE  
    (l.beer='Budweiser' OR l.beer='Bud') AND  
    d.phone LIKE '917%' AND  
    d.name = l.drinker
   ```

	# drinker


### 2. What beers does Mike like?
```sql
SELECT DISTINCT beer FROM Likes WHERE drinker='Mike'
```

	# beer
	
	Blue Moon  
	Bud  
	Budweiser  
	Creamy Dark  
	Hefeweizen  
	Michelob Golden Draft Light  
	Original Premium Lager  
	Original Premium Lager Dog  
	Killian's

### 3. Which town has the most drinkers?
```sql
SELECT city  
FROM Drinkers  
GROUP BY city  
ORDER BY count(*) DESC  
LIMIT 1;
```

	# city
	
	San Francisco

### 4. What bars are frequented by drinkers from that town (3)?
```sql
SELECT DISTINCT bar  
FROM Frequents f, Drinkers d  
WHERE d.name = f.drinker AND  
    d.city = 'San Francisco';
```

	# bar
	'Blue Angel'  
	'Coconut Willie\'s Cocktail Lounge'  
	'The Blank Club'

### 5. Provide all bars which serve beers that Mike likes
```sql
SELECT DISTINCT s.bar  
FROM Sells s, (SELECT beer FROM Likes WHERE drinker='Mike') AS b  
WHERE s.beer = b.beer;
```

	# bar
	
	A.P. Stump's  
	Blue Angel  
	Blue Tattoo  
	Britannia Arms  
	Cabana  
	Caravan  
	Club 175  
	Coconut Willie's Cocktail Lounge  
	Gecko Grill  
	Giza Hookah Lounge  
	Hedley Club  
	Seven Bamboo  
	The Backbeat  
	The Blank Club  
	The Shark and Rose


### 6. Who likes at least one same beer that Joe or Mike like?

```sql
SELECT DISTINCT l.drinker  
FROM Likes l, Likes l1, Likes l2  
WHERE  
    (l.beer = l1.beer OR l.beer = l2.beer)  
    AND  l.drinker != 'Joe' AND l.drinker != 'Mike';
```

	# drinker
	
	John  
	Justin  
	Vince  
	Jesse


### 7.  All bars which sell at least one beer which is liked by at least one drinker who frequents these bars
```sql
SELECT DISTINCT s.bar  
FROM Sells s, Frequents f, Likes l  
WHERE f.bar = s.bar AND  
    s.beer = l.beer AND  
    f.drinker = l.drinker;
```

	# bar
	
	A.P. Stump's  
	Blue Angel  
	Cabana  
	Caravan  
	Gecko Grill  
	Seven Bamboo  
	The Shark and Rose


### 8. Drinkers who like some beers sold by Caravan bar
```sql
SELECT DISTINCT l.drinker  
FROM Likes l, Sells s  
WHERE l.beer = s.beer AND s.bar = 'Caravan'  
GROUP BY l.drinker HAVING count(*) > 1;
```

or…

```sql
SELECT DISTINCT l.drinker  
FROM Likes l, (SELECT beer FROM Sells WHERE bar='Caravan') AS s  
WHERE l.beer = s.beer  
GROUP BY l.drinker HAVING count(*) > 1;
```

	# drinker
	
	John  
	Mike  
	Vince

### 9. Bars which sell Budweiser and are frequented by some drinkers who like Budweiser
```sql
SELECT DISTINCT b.bar
FROM 
	(SELECT DISTINCT bar FROM Sells WHERE Sells.beer = 'Budweiser') as b,
    Frequents f,
    Likes l
WHERE
	f.drinker = l.drinker
    AND l.beer = 'Budweiser'
    AND f.bar = b.bar
```
	
	# bar
	'Cabana'
	'Caravan'
	'Gecko Grill'
	'Seven Bamboo'
	'The Shark and Rose'

### 10.  Bars which are frequented by Mike and Steve

### 11. Drinker who like at least two beers that Mike likes
```sql
SELECT COUNT(*), drinker
FROM Likes l1
WHERE beer in (
	SELECT beer
    FROM Likes l
    WHERE
		l.drinker = 'Mike'
        AND l1.drinker!=l.drinker
	)
GROUP BY l1.drinker
HAVING COUNT(*)>1
```
	# COUNT(*), drinker
	'5', 'John'
	'2', 'Justin'


### 12. Bars which sell at least 3 beers that Mike likes (do not use COUNT)



#self_join
