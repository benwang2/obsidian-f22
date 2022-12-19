---
title: Lecture Notes 25
course: CS_352
date: 2022-12-19
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 25</h1></center>

## Computing the Forwarding table
- Suppose a router in AS1 to forward a packet destined to external prefix X.
- How is the forwarding table entry for X at 1d computed?
- How is the forwarding table entry for X at 1c computed?

### eBGP and iBGP announcements
- AS2 router 2c receives path announcements AS3,X (via **eBGP**) from router 3a
- Based on AS2 import policy, AS2 router 2c imports and selects path AS3,X, propagates (via iBGP) to all AS2 routers
- Based on AS2 export policy, AS2 router 2a announces (via eBGP) path AS2, AS3,X to AS1 router 1c

A router may learn about **multiple** paths to a destination:
- AS1 gateway router 1c learns path AS2, AS3, X from 2a (next hop 2a)
- AS1 gateway router 1c learns path AS3, X from 3a (next hop 3a)
- Through BGP route selection process, AS1 gateway router 1c chooses path AS3,X, and announces path within AS1 via iBGP

## Setting forwarding table entries
 