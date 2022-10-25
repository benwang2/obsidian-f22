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

Apps that read from receive-side socket buffer when you do a `recv()` call.

However, applications do not always read from the socket immediately.

The receiver's TCP stack deposits the data in the receive-side socket buffer. Some TCP code from the sender deposits data within the TCP socket receiver buffer, which the application process can then receive with `sock.recv()`.

The 