---
title: Lecture Notes 14
course: CS_352
date: 2022-10-25
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 14</h1></center>
## Buffering and Ordering in TCP
TCP uses **selective repeat**, so the receiver must **buffer** data received after loss.
#selective_repeat

Apps that read from receive-side socket buffer when you do a `recv()` call.

However, applications do not always read from the socket immediately.

The receiver's TCP stack deposits the data in the receive-side socket buffer. Some TCP code from the sender deposits data within the TCP socket receiver buffer, which the application process can then receive with `sock.recv()`.

Data can not be immediately discarded from the sender once transmitted. This is because of the possibility of packet re-transmission.

TCP receiver software only releases data from receive-side socket buffer once the data is in order relative to all other data read by application.

Individual packets can be dropped in transmission such that a retransmitted packet will cause the packets to be out of order. Therefore, we need a process to reorder the packets in the buffer. This process is called **TCP reassembly**.

#tcp_reassembly

The receiver-side socket buffer can only contain so much out-of-order data. As a consequence, any subsequent out-of-order packets are dropped. Additionally, if there is too much packet reordering, the TCP application-level throughput will suffer.

## Stream-Oriented Data Transfer
TCP is a stream-oriented data transfer, meaning that a TCP socket will receive data in a continuous stream. When `sock.recv(n)` is called, $n$ bytes will be read from the socket side buffer.