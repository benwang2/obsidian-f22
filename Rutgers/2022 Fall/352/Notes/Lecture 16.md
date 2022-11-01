---
title: Lecture Notes 16 
course: CS_352
date: 2022-11-01
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 16</h1></center>

## Congestion Control

The internet uses a **distributed algorithm** to converge to an **efficient** and **fair** outcome.

With this algorithm, each endpoint acts on its own - there is no central vantage point or control.

To make the congestion control *efficient*, Maximize the amount of bottleneck capacity used, even with a single TCP connection.

To make the congestion control *fair*, we share the bottleneck capacity equitably.

### Signals and Knobs
We use signals and knobs to adjust the congestion control effectively.

**Signals**
- Packet ACKed
- Packet dropped (RTO)
- Packet delayed (RTT)
- Rate of incomings ACKs

These are **implicit** feedback signals measured directly at the sender.
#ACK #RTO #RTT

**Knobs** are something you use to "probe" the available bottleneck capacity

### Sense and React
With sense and react, we ideally want to be in the **steady state**, which we achieve using congestion control algorithms.

**Ideal Goal**
We want to achieve a **high sending rate**, which we accomplish by using the full capacity of the bottleneck link.
We also want **low delay**, which minimizes overall delay of packets to get to the receiver
- Overall delay = propagation + queuing + transmission
- assume propagation and transmission are fixed

If we have a fast link, and a bottleneck link, the the packets will take longer to send. This will result in the packets having a delay between receiving. This is called **inter-packet delay**.

**ACK clocking**: when the sender receives an ACK, it must be safe to send another packet without congesting the bottleneck link.

### Steady State
