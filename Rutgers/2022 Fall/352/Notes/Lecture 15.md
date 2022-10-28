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