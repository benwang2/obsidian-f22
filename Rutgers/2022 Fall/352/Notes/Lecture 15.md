---
title: Lecture Notes 15
course: CS_352
date: 2022-10-28
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 15</h1></center>

## Flow Control
### Bottlenecks
- Maximum rate a user can push data is determine by three bottlenecks
	1. Application process
	2. TCP Socket receiver buffer
	3. Link between source router and destination router

#bottleneck #tcp
### Drops due to Buffer Fill
The TCP sender can only buffer so much information before dropping subsequent data.

At bottlenecks, data begins to be dropped is full. So, we can avoid drops due to buffer fill by having the TCP sender only transmit as much as the **free buffer space**.

The amount of empty space in the buffer is known as the **advertised window size**, which is included in the receiver's ACK.

The sender's sliding window can not be larger than the advertised window, to avoid dropped packets.

#sliding_window

If a receiver app is reading data too slowly,
- receiver socket buffer fills up
- advertised window shrinks
- sender's window shrinks
- sender's sending rate reduces

**Flow control** matches the sender's write speed to the receiver's read speed.

If the socket buffer is too small, the sender can't keep too many packets in flight, resulting in **lower throughput**.

If the socket buffer is too large, too much memory is consumed per socket.

### Size of a Receiver Socket Buffer
- **Case 1**: The receiving app is reading too slowly
	- There is no amount of receiver buffer that can prevent low throughput
- **Case 2**: The receiving app reads sufficiently fast on average to match the sender's writing speed
	- Receiver must use buffer of size at least W.

The **correct socket buffer sizing** is essential to maximize TCP throughput.

## Congestion Control
Routers use **buffers** to accomodate queued packets. Any packets beyond the max buffer will be dropped.

The **link load** is the fraction of link used.

When there are too many retransmissions due to packet drops, the amount of useful data plummets. This is called a **congestion collapse**.

As the link load increases, so does the queuing delay.

### Bottlenecks
When multiple endpoints share a network, it becomes difficult to
- identify the bottleneck link
- know how many other endpoints are using the link

Endpoints may join and leave at any time and network paths may change over time, leading to different links bottlenecking over time.

The solution to this is to use a **distributed algorithm** that converges to a **fair and efficient outcome**. With this approach, no single entity can control or view all endpoints and bottlenecks, and each endpoint must try to reach a globally good outcome. As a result, a lot of trust is **given to endpoints**.

For N endpoints, each should get 1/N'th of link capacity.

| Flow Control                          | Congestion Control                 |
| ------------------------------------- | ---------------------------------- |
| avoid overwhelming receiver           | avoid overwhelming bottleneck link |
| sender manages receiver socket buffer | sender manages bottleneck link capacity and bottleneck router buffers

### Signals and Knobs in Congestion control
The internet uses a distributed algorithm to converge to an efficient and fair outcome, which we achieve using by **sensing and reacting**. It makes use of a **feedback loop** with signals and knobs

#### Signals
A signal is an event that occurs that we measure and determine whether to adjust the network.
For example,
- packets being ACK'ed
- packets being dropped
- packets being delayed (RTT)
- rate of incoming ACKs

#### Knobs
A knob is something you can change to "probe" the available bottleneck capacity.
For example,
- increase window/sending rate
- decrease window/sending rate

We make use of signals and knobs to get to the **steady state**.