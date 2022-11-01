---
title: Lecture Notes 15 
course: CS_352
date: 2022-11-01
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 15</h1></center>
## Topics Covered
- NoSQL

## NoSQL databases
NoSQL implements semistructured data and is better for unstructured data that needs to be scalable.

### Not First Normal Form
A relational database must be in first normal form, but a NoSQL database does not have to conform to normal form.

### Benefits
NoSQL databases can contain a lot of different types:
- HTML
- Images
- Text

#### Semistructured data
Semistructured data is data that is annotated by its fields, as opposed to a schema, tables, and attributes.

#### Denormalization
With NoSQL, every resource is not required to have an attribute or to be *normalized*. We don't have to worry about relations as much because there's no need for artificially created tables.

### Detriments
However, **there's no standard query language** for NoSQL databases. A lot of features that are standard in SQL are not implemented in NoSQL.

### When to use NoSQL?
NoSQL is recommended when
- there is no need for "ad hoc queries", where we are just using a bounded set of queries.
- we have semi-structured data
- elastic consistency

### Complexity of Queries
#### Simple queries
...

#### Complex Queries
...

## Quiz
