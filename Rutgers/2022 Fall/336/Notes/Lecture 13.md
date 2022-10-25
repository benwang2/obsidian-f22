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

## Functional Dependencies and Boyce-Codd Normal Form (BCNF)
If $X \rightarrow A$ is a **functional dependency** satisfied by scheme R, then X is a superkey.

A **functional dependency** is a constraint that defines a relation such that $X \rightarrow A$ , or "X determines A".

### Functional Dependency
For a schema, $Drinkers(name, addr, beersLiked, manf, favBeer)$ we could reasonably assert
1. $name \rightarrow favBeer$
2. $beersLiked \rightarrow manf$

Functional dependencies are constraints that databases much satisfy.

A one-to-many relationship implies a functional dependency from the many-to-one side.
A one-to-one relationship implies a bidirectional functional dependency.

Another example is: "no two courses can meet in the same room at the same time" (hour, room -> course)

### Keys of Relations
Key $K$ is a **superkey** if for relation $R$ if $K$ functionally determines all of $R$.
Key $K$ is a **key** for $R$ if $K$ is a *superkey*, but no proper subset of K is a superkey.

### Superkey
For a schema, $Drinkers(name, addr, beersLike, manf, favBeer)$
- $\{name, beersLiked\}$ is a superkey because together these attributes determine all other attributes
	- $name \rightarrow addr, favBeer$
	- $beersLiked \rightarrow manf$

### Key
For the same schema, $\{name, beersLiked\}$ is a key.

To add a key, we can simply assert a key $K$. Alternatively, we can assert functional dependencies and deduce keys by systematic exploration.

## Closure Test
A closure test is a recursive algorithm that recursively computes the closure of $Y$, which is denoted as $Y^+$.

**Basis**: Let $Y^+=Y$
**Induction:** Look for a functional dependency's left side $X$ such that it is a subset of the current $Y+$. If the FD is $X \rightarrow A$, we add $A$ to $Y^+$

We know if something is a superkey if we test the closure and all attributes are functional dependencies.

## Relational Schema Design
**Update anomaly**: Update of one value causes multiple tuples to be updated
**Deletion anomaly**: Unintended loss of a piece of information as result of unrelated or weak related deletion
**Redundancy**: Repeating the same info

## Quiz Questions
- A **functional dependency** is either many-to-one, or one-to-one
- A **superkey** is a subset which determines all attributes.
- What is a closure of the set of attributes? The set of all attributes determined by that setIs Penna table in BCNF?