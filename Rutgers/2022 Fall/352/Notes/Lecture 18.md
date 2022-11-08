---
title: Lecture Notes 18 
course: CS_352
date: 2022-11-08
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 18</h1></center>

## Handling Packet Loss
...
### Detecting packet loss
...

### Retransmitting data
Distinction: In-flight versus window

#### TCP fast retransmit

Reduce cwnd and in-flight gently, (don't drop cwnd to 1 MSS)

So, we reduce the amount of in-flight data **multiplicatively** by setting $inflight \rightarrow inflight/2$. Set $cwnd = (inflight / 2) + 3MSS$.

This operation is called the **multiplicative decrease**.

This algorithm also $ssthresh$ to $inflight / 2$
