---
title: Lecture Notes 14
course: CS_XXX
date: 2022-10-25
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 14</h1></center>
## Buffering and Ordering in TCP
TCP uses **selective repeat**, so the receiver must **buffer** data received after loss.

Apps thatread from receive-side socket buffer when you do a recv()