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
For a priamry index, the selectivity is on