1. Bars which sell at least one beer liked by a resident of Edison
```sql
SELECT DISTINCT s.bar
FROM
	Sells s,
    (SELECT beer FROM Drinkers d, Likes l WHERE d.city = 'Edison') as b
WHERE
	s.beer = b.beer;
```
	Caravan
	Britannia Arms
	Cabana
	Club 175
	Coconut Willie's Cocktail Lounge
	Gecko Grill
	Giza Hookah Lounge
	Seven Bamboo
	The Blank Club
	The Shark and Rose
	A.P. Stump's
	Hedley Club
	Blue Tattoo
	The Backbeat
	Blue Angel

2. Beers which are liked by Mike and by Devarsh
   ```sql
SELECT DISTINCT l.beer
FROM
	Likes l,
    Likes l1
WHERE
	l.drinker = 'Mike' AND 
    l1.drinker = 'Devarsh' AND 
    l.beer = l1.beer
```
	Blue Moon

3. Drinkers who do not frequent Caravan bar
```sql
SELECT DISTINCT d.name
FROM Drinkers d
WHERE d.name NOT IN (
		SELECT f.drinker
        FROM Frequents f
        WHERE f.bar = 'Caravan'
);
```
	Ahmed
	Ajla
	Bob
	Boshen
	Devarsh
	Erik
	Gunjan
	Harshal
	Herb
	Jeanie
	Jesse
	Kayla
	Laura
	Mike
	Rebecca
	Sahil
	Tatiana
	Vedant
	Vince
	Vishal
	Yuchen
	Yuhan

4. Bars which sell most beers under $6 (include ties)
```sql
SELECT bar
FROM Sells
WHERE price < 6
GROUP BY bar
HAVING COUNT(*) = (
	SELECT COUNT(*)
	FROM Sells
	WHERE price < 6
	GROUP BY bar 
	ORDER BY COUNT(*) DESC
	LIMIT 1
);
```
	The Shark and Rose
5. Bars which sell all beers
```sql
SELECT DISTINCT s.bar
FROM Sells s
WHERE NOT EXISTS(
	SELECT name
	FROM Beers b
	WHERE name NOT IN (SELECT beer FROM Sells WHERE bar=s.bar)
);
```
	None

6. Use left join to find Drinkers who do not frequent Caravan bar
7. Use Case statement to add new attribute to Sells table with two values:  "Expensive" and "Regular".

Expensive are beers sold above $8, The remaining beers are "Regular".
8. Which precinct(s) had the highest totalvotes at the end of voting?
9. Extract domain name from www.cs.rutgers.edu/~rmartin
10. How many votes did Biden get by the end of the day of November 6, 2020?
