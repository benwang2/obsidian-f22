---
title: Lecture Notes 15
course: CS_352
date: 2022-10-28
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 15</h1></center>


## Bottlenecks
- Maximum rate a user can push data is determine by three bottlenecks
	1. Application process
	2. TCP Socket receiver buffer
	3. Link between source router and destination router

### Drops due to Buffer Fill
At bottlenecks, data begins to be dropped is full. So, we can avoid drops due to buffer fill by having the TCP sender only transmit as much as the **free buffer space**.

The amount of empty space in the buffer is known as the 