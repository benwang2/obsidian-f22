--
title: Lecture Notes 12
course: CS_352
date: 2022-10-18
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 12</h1></center>

## RTO
A good RTO predict the round-trip time (RTT) between sender and receiver. 

If an ACK hasn't been returned within our estimated RTT, the packet was likely dropped. RTT can be measured directly at sender - no receiver or router help is needed. 