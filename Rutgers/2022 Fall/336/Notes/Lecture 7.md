---
title: Lecture Notes 7
course: CS_336
date: 2022/10/04
tags: 
- lectureNotes
- CS_336
---

<center><h1>Lecture 7</h1></center>
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

#### Clustered indexes
Clustered indexes sort and store the data rows in the table or view based on their key values. For each table, there can only be one clustered index because the data rows themselves can be stored in only one order.

A table is only ever sorted when it contains a clustered index. Otherwise, the data rows are stored in an unordered structure called a heap.

#### Nonclustered indexes
Nonclustered indexes have a structure seperate from the data rows. A nonclustered index contains the nonclustered index key values and each eky value entry has a pointer to the data row that contains the key value.

The pointer from an index row in a nonclustered index to a data row is called a row locator. The structure of the row locator depends on whether the data pages are stored in a heap or a clustered table. For a heap, a row locator is a pointer to the row. For a clustered table, the row locator is the clustered index key.
<sub><a href="https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver16">source (clustered and nonclustered indexes)</a></sub>

You can add nonkey columns to the leaf level of the nonclustered index to by-pass existing index key limits, and execute fully covered, indexed, queries.

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
With a secondary index on beer, it will be $log(size(beers)) + io$, where $io$ is the number of file read/writes to get all bars which serve heineken.

With joins, the benefits of indexing are increasingly visible. Queries that were cripplingly slow become trivial to run.