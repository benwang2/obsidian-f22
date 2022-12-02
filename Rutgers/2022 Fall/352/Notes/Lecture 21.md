---
title: Lecture Notes 21
course: CS_352
date: 2022-11-29
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 21</h1></center>
## Router design
A router contains the **control plane** and the **data plane**.

The control plane manages routing of the information, following **traditional distributed routing**. There is per route-change processing every few tens of seconds.

The **data plane** performs per-packet processing every few tens of nanoseconds.

## Control processor (plane)
The control processor is a general-purpose processor that "programs" the data plane:
- uses forwarding table
- manages scheduling and buffer management policy

It implements the **routing algorithm** by processing **routing protocol messages**.

