---
title: Lecture Notes 7
course: CS_336
date: 2022/10/04
tags: 
- lectureNotes
- CS_336
---

# Lecture 7
## Topics Covered
- CREATE INDEX
- PRIMARY Keyword
- FULLTEXT Keyword
- Indexing selectivity
	- primary, unique: selectivity = 1

## Indexes
An SQL index is used to retrieve data from a database very quickly. Indexing a table or view helps to improve the performance for databases. There are many different ways to index a table.

One common way to index a table is by adding a **primary index** on a set of fields that includes the unique primary key for the field and guarantees no duplicates.

Another way to index a table is to use secondary indexes. Secondary indexes are normal, non-unique indexes.

Primary and secondary indexes are typically implemented internally by using b-trees, which allow for selecting and sorting ranges, or hash tables.

Finally, there are FULLTEXT indexes. These indexes are useful only for full text searches done with MATCH() and AGAINST() clauses.

### Index Selectivity
For a primary and unique index, the selectivity is one.
For a secondary index, the selectivity is greater than one.

When selecting an index, we always want to select an index with a smaller value of selectivity.

### Implementation
How is it implemented?

### Benefits of indexing
Effectively setting an index can reduce the runtime of queries drastically. The example provided is:
```sql
SELECT * FROM Sells WHERE beer='Heinekn'
```
With no index, this query executes in $O(n)$ time, where *n* is the size of Sells.
With a secondary index on beer, it will be $log(size(beers)) + I