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
        "") Result
FROM
    penna
GROUP BY precinct
HAVING Result != "";
```

	# Result
	'Adams Township - Dunlo Voting Precinct'
	'Adams Township - Elton Voting Precinct'
	'Adams Township - St. Michael Voting Precinct'
	'Adams Township No. 1 Voting Precinct'
	'Adams Township- - Gramlingtown Voting Precinct'
	'Allegheny Township Voting Precinct'
	'Ashville Borough Voting Precinct'
	'Barr Township Voting Precinct'
	'Blacklick Township Voting Precinct'
	'Brownstown Borough Voting Precinct'
	'Cambria Township - Colver Voting Precinct'
	'Cambria Township - Revloc Voting Precinct'
	'Cambria Township No. 1 Voting Precinct'
	'Cambria Township No. 4 Voting Precinct'
	'Carrolltown Borough Voting Precinct'
	'Chest Township Voting Precinct'
	'Clearfield Township Voting Precinct'
	'Conemaugh Township - Center Voting Precinct'
	'Conemaugh Township - Cover Hil Voting Precinct'
	'Cresson Borough Voting Precinct'
	'Cresson Township - North Voting Precinct'
	'Cresson Township - South Voting Precinct'
	'Croyle Township - No. 2 Voting Precinct'
	'Croyle Township No. 1 Voting Precinct'
	'Daisytown Borough Voting Precinct'
	'Dale Borough Voting Precinct'
	'Dean Township Voting Precinct'
	'East Carroll Township - North Voting Precinct'
	'East Carroll Township - South Voting Precinct'
	'East Conemaugh Borough Voting Precinct'
	'East Taylor Township - No. 1 Voting Precinct'
	'East Taylor Township No. 2 Voting Precinct'
	'Ebensburg Borough - Center Voting Precinct'
	'Ebensburg Borough - East Voting Precinct'
	'Ebensburg Borough - West Voting Precinct'
	'Elder Township Voting Precinct'
	'Ferndale Borough Voting Precinct'
	'Gallitzin Borough Voting Precinct'
	'Gallitzin Township Voting Precinct'
	'Geistown Borough No. 1 Voting Precinct'
	'Geistown Borough No. 2 Voting Precinct'
	'Hastings Borough Voting Precinct'
	'Jackson Township - Vinco Voting Precinct'
	'Jackson Township No. 1 Voting Precinct'
	'Jackson Township No.3 Voting Precinct'
	'Johnstown - Eighteenth Ward Voting Precinct'
	'Johnstown - Eighth Ward No. 1 Voting Precinct'
	'Johnstown - Eighth Ward No. 3 Voting Precinct'
	'Johnstown - Nineteenth Ward Voting Precinct'
	'Johnstown - Twenty-first Ward Voting Precinct'
	'Johnstown -17th Ward 2 Voting Precinct'
	'Johnstown -17th Ward 3 Voting Precinct'
	'Johnstown-20th Ward 1 Voting Precinct'
	'Lilly Borough - First Ward Voting Precinct'
	'Lilly Borough - Second Ward Voting Precinct'
	'Lorain Borough Voting Precinct'
	'Loretto Borough Voting Precinct'
	'Lower Yoder Township No. 2 Voting Precinct'
	'Lower Yoder Township No.1 Voting Precinct'
	'Middle Taylor Township Voting Precinct'
	'Munster Township Voting Precinct'
	'Nanty Glo Borough - First Ward Voting Precinct'
	'Nanty Glo Borough - Second War Voting Precinct'
	'Northern Cambria Borough - Cen Voting Precinct'
	'Northern Cambria Borough - Nor Voting Precinct'
	'Northern Cambria Borough - Sou Voting Precinct'
	'Patton Borough - First Ward Voting Precinct'
	'Patton Borough - Second Ward Voting Precinct'
	'Portage Borough - First Ward Voting Precinct'
	'Portage Borough - Second Ward Voting Precinct'
	'Portage Borough - Third Ward Voting Precinct'
	'Portage Township - Southwest Voting Precinct'
	'Portage Township Center Voting Precinct'
	'Reade Township Voting Precinct'
	'Richland Township No. 1 Voting Precinct'
	'Richland Township No. 2 Voting Precinct'
	'Richland Township No. 3 Voting Precinct'
	'Richland Township No. 4 Voting Precinct'
	'Richland Township No. 5 Voting Precinct'
	'Richland Township No. 6 Voting Precinct'
	'Richland Township No. 7 Voting Precinct'
	'Richland Township No. 8 Voting Precinct'
	'Richland Township No. 9 Voting Precinct'
	'Sankertown Borough Voting Precinct'
	'Scalp Level Borough Voting Precinct'
	'South Fork Borough Voting Precinct'
	'Southmont Borough No. 1 Voting Precinct'
	'Southmont Borough No. 2 Voting Precinct'
	'Stonycreek Township - Ward 1 Voting Precinct'
	'Stonycreek Township - Ward 2 Voting Precinct'
	'Stonycreek Township - Ward 3 Voting Precinct'
	'Stonycreek Township - Ward 4 Voting Precinct'
	'Summerhill Borough Voting Precinct'
	'Summerhill Township - North Voting Precinct'
	'Summerhill Township - South Voting Precinct'
	'Susquehanna Township - North Voting Precinct'
	'Susquehanna Township - South Voting Precinct'
	'Tunnelhill Borough Voting Precinct'
	'Upper Yoder Township No. 1 Voting Precinct'
	'Upper Yoder Township No. 2 Voting Precinct'
	'Upper Yoder Township No. 3 Voting Precinct'
	'Upper Yoder Township No. 4 Voting Precinct'
	'Vintondale Borough Voting Precinct'
	'Washington Township Voting Precinct'
	'West Carroll Township - North Voting Precinct'
	'West Carroll Township - South Voting Precinct'
	'West Taylor Township Voting Precinct'
	'Westmont Borough No. 1 Voting Precinct'
	'Westmont Borough No. 2 Voting Precinct'
	'Westmont Borough No. 3 Voting Precinct'
	'White Township Voting Precinct'
	'Wilmore Borough Voting Precinct'
	'BELLEFONTE SOUTHEAST'
	'BENNER NORTH'
	'BENNER SOUTH'
	'BOGGS EAST'
	'BOGGS WEST'
	'BURNSIDE'
	'CURTIN SOUTH'
	'FERGUSON WEST'
	'GREGG'
	'HAINES'
	'HALFMOON EAST CENTRAL'
	'HALFMOON PROPER'
	'HOWARD BORO'
	'HOWARD TWP'
	'HUSTON'
	'MARION'
	'MILES EAST'
	'MILES WEST'
	'MILESBURG'
	'MILLHEIM'
	'PENN'
	'PHILIPSBURG 2ND WARD'
	'PHILIPSBURG 3RD WARD'
	'PORT MATILDA'
	'POTTER NORTH'
	'POTTER SOUTH'
	'RUSH NORTH'
	'RUSH NORTH CENTRAL'
	'RUSH SOUTH'
	'RUSH WEST'
	'SNOW SHOE'
	'SNOW SHOE EAST'
	'SNOW SHOE WEST'
	'SPRING EAST'
	'SPRING SOUTH'
	'SPRING SOUTHWEST'
	'SPRING WEST'
	'TAYLOR'
	'UNION'
	'UNIONVILLE'
	'WALKER WEST'
	'WORTH'
	'Aleppo Voting Precinct'
	'Carmichaels Borough Voting Precinct'
	'Center Voting Precinct'
	'Clarksville Borough Voting Precinct'
	'Cumberland #1 Voting Precinct'
	'Cumberland #2 Voting Precinct'
	'Cumberland #4 Voting Precinct'
	'Cumberland Nemacolin Voting Precinct'
	'Dunkard #1 Voting Precinct'
	'Dunkard #2 Voting Precinct'
	'Franklin East Voting Precinct'
	'Franklin North Voting Precinct'
	'Franklin South Voting Precinct'
	'Franklin West Voting Precinct'
	'Freeport Voting Precinct'
	'Gilmore Voting Precinct'
	'Gray Voting Precinct'
	'Greene Voting Precinct'
	'Greensboro Borough Voting Precinct'
	'Jackson Voting Precinct'
	'Jefferson #1 Voting Precinct'
	'Jefferson #3 Voting Precinct'
	'Jefferson #4 Voting Precinct'
	'Jefferson Borough Voting Precinct'
	'Monongahela #1 Voting Precinct'
	'Monongahela #2 Voting Precinct'
	'Morgan - Lippencott Voting Precinct'
	'Morgan - Mather Voting Precinct'
	'Morgan Chart/tgrdn Voting Precinct'
	'Morris Voting Precinct'
	'Perry Voting Precinct'
	'Rices Landing Borough Voting Precinct'
	'Richhill Voting Precinct'
	'Springhill Voting Precinct'
	'Washington Voting Precinct'
	'Wayne - East Voting Precinct'
	'Wayne - West Voting Precinct'
	'Waynesburg #1 Voting Precinct'
	'Waynesburg #2 Voting Precinct'
	'Waynesburg #3 Voting Precinct'
	'Whiteley Voting Precinct'
	'Bridgeport 2'
	'Collegeville 1'
	'East Norriton 1-1'
	'Franconia 4'
	'Franconia 5'
	'Hatfield 2-2'
	'Hatfield 5-1'
	'Souderton 2'
	'Towamencin 2-3'
	'Worcester East 3'



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