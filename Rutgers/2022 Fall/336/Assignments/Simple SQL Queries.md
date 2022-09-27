---
title: Simple SQL Queries
course: CS_336
released: 2022/09/22
due: 2022/10/07
tags: Assignments
---
<center><h1>Simple SQL Queries</h1></center>
<center><h3>CS 210 - Principles of Information and Data Management</h3></center>

Return SQL code as text file plus results which workbench gave you (you can include them in the same txt file). Query + answer. As long as it is readable by a grader, it is fine - text, word, screenshot....but text is easiest.   

### 1.  Find all distinct drinkers whose phone numbers come from area code 917 and who like Budweiser or Bud (synonim!)
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

  
'Blue Angel'  
'Coconut Willie\'s Cocktail Lounge'  
'The Blank Club'
### 5. Provide all bars which serve beers that Mike likes

### 6. Who likes at least one same beer that Joe or Mike like?

### 7.  All bars which sell at least one beer which is liked by at least one drinker who frequents these bars

### 8. Drinkers who like some beers sold by Caravan bar

### 9. Bars which sell Budweiser and are frequented by some drinkers who like Budweiser

### 10.  Bars which are frequented by Mike  and Steve

### 11. Drinker who like at least two beers that Mike likes

### 12. Bars which sell at least 3 beers that Mike likes (do not use COUNT)