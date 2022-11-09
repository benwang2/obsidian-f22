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

(1) Reduce cwnd and in-flight gently, (don't drop cwnd to 1 MSS)

So, we reduce the amount of in-flight data **multiplicatively** by setting $inflight \rightarrow inflight/2$. Set $cwnd = (inflight / 2) + 3MSS$.

This operation is called the **multiplicative decrease**.

This algorithm also $ssthresh$ to $inflight / 2$

(2) The seq# from dup ACKs is **immediately retransmitted**. So, we **don't wait for an RTO** if there's strong evidence that a packet was lost.

Sender keeps the reduced $inflight$ until a new ACK arrives, and conserves the packets in flight.

We will keep increment cwnd for each duplicate ACK.

Eacj

### TCP fast recovery
The sender keeps the reduced *inflight* until a **new ACK** arrives and conserves the packets in flight. Conserving packets in flight allows for some data to be transmitted over lossy periods.

For each duplicate ACK, we increment $cwnd$ by 1 MSS.