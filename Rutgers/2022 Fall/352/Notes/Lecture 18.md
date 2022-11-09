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
Data that is **in-flight** is data that is currently in transmission, whereas the window is what the sender seeks to fulfill.

Simply, the window defines the range of data that is to be received. Data in-flight is data that has  yet to be received.

#### TCP fast retransmit
Once we are certain that packets are dropped (determine by observing duplicate ACKs), we will...

(1) Reduce cwnd and in-flight gently, (don't drop cwnd to 1 MSS)

$MSS$ = Maximum segment size

So, we reduce the amount of in-flight data **multiplicatively** by setting $inflight \rightarrow inflight/2$. Set $cwnd = (inflight / 2) + 3MSS$.

This operation is called the **multiplicative decrease**.

This algorithm also sets $ssthresh$ to $inflight / 2$

(2) The seq# from dup ACKs is **immediately retransmitted**. So, we **don't wait for an RTO** if there's strong evidence that a packet was lost.

Sender keeps the reduced $inflight$ until a new ACK arrives, and conserves the packets in flight.

We will keep increment cwnd for each duplicate ACK, because we know a packet has been received and we can transmit another.

Each ACK is transmitted alongside a cumulative ACK, which specifies what packets we want to receive. As we receive more duplicate ACKs in the cumulative ACK, we know that we've most likely dropped this packet.


### TCP fast recovery
The sender keeps the reduced *inflight* until a **new ACK** arrives and conserves the packets in flight. Conserving packets in flight allows for some data to be transmitted over lossy periods.

For each duplicate ACK, we increment $cwnd$ by 1 MSS.

We keep the $inflight$ value until a new ACK arrives, then we have recovered from a network loss.

Only then are we able to consider increasing the amount $inflight$.

When we finally receive a new ACK, we can then acknowledge the retransmitted data and all data inbetween.

Following this, we will deflate $cwnd$ to half of $cwnd$ before fast retransmit.

### Additive Increase & Multiplicative Decrease
We may assume that the network has dropped packets if there is a **triple duplicate ACK**. 

When this occurs, we perform a **fast re-transmit**. This drops the amount $inflight = inflight/$