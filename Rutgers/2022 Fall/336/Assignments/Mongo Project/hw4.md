---
title: Project Mongo
course: CS_336
released: YYYY-MM-DD
due: YYYY-MM-DD
tags:
- Assignments
- CS_336
---
<center><h1>Project Mongo</h1></center>
<center><h3>CS336</h3></center>
1. Return the bar if either its phone or address is an empty string.
```javascript
use db;
db.Bar.find({"$or":[{"addr":""},{"phone": ""}]})
```
2. Find the city that has more than 4 bars. Return the city name and the number of bars it has.
```javascript
use db;
db.Bars.aggregate([
  {
    "$group": {
      "_id": "$city",
      "count": {
        "$sum": 1
      }
    },
  },
  {
    "$match": { "count": { "$gt": 4 } }
  }
]);
```
3. Return how many bars sell more than 5 kinds of beers.
```javascript
use db;
db.Bars.aggregate([
    {
      "$project": {
        "name": 1,"num_sold": {"$size": "$beers"}
      },
    },
    {"$match" : {"num_sold": {"$gt": 5}}}
])

```
4. Find the drinkers that have visited any bars either on Saturday or Sunday (or both) \[hint: go check out "$elemMatch" function\]
```javascript
use db;
db.Drinkers.find(
  {
    "history": {
      "$elemMatch": {
        "day": { "$in": ["Saturday", "Sunday"] }
      }
    }
  }
);
```
5. Find the drinker who has ordered "Blue Tattoo" beer more than once
6. Insert Lucy to Drinker collection. Lucy is from Edison, lives at "433 River Road" with phone number 732-571-9871, she is 23 years old and her list of favorite bar foods consists of: French fries, onion rings, nachos, and wings.
7. **Value count**: Given a relation R, represent R as JSON object J with the *smallest value count*
8. For each timestamp T, define TotIncrement as sum of totalvote increments over all precincts (totalvote increment, as defined in 2.1 of Election project newPenna). Finds timestamp(s) with largest value of TotIncremenet along with this largest value. Submit CODE and result.