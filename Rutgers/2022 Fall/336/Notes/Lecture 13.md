---
title: Lecture Notes 13
course: CS_336
date: 2022-10-25
tags: 
- lectureNotes
- CS_336
---

<center><h1>Lecture 13</h1></center>

## Topics Covered
- Functional dependencies
- BCNF

### Functional Dependencies and Boyce-Codd Normal Form (BCNF)
If $X \rightarrow A$ is a **functional dependency** satisfied by scheme R, then X is a superkey.

A **functional dependency** is a constraint that defines a relation such that $X \rightarrow A$ , or "X determines A".

### Functional Dependency
For a schema, $Drinkers(name, addr, beersLiked, manf, favBeer)$ we could reasonably assert
1. $name \rightarrow favBeer$
2. $beersLiked \rightarrow manf$

Functional dependencies are constraints that databases much satisfy.

A one-to-many relationship implies a functional dependency from the many-to-one side.
A one-to-one relationship implies a bidirectional functional dependency.

### Keys of Relations
Key $K$ is a **superkey** if for relation $R$ if $K$ functionally determines all of $R$.
Key $K$ is a **key** for $R$ if $K$ is a *superkey*, but no proper subset of K is a superkey.

### Superkey
For a schema, $Drinkers(name, addr, beersLike, manf, favBeer)$
- $\{name, beersLiked\}$ is a superkey because together these attributes determine all other attributes
	- $name \rightarrow addr, favBeer$
	- $beersLiked \rightarrow manf$


### Quiz Questions
- A **superkey** is a subset which determines all attributes.
- 