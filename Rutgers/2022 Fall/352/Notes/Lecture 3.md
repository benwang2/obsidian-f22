---
title: Lecture Notes 3
course: CS_352
date: 2022/09/13
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 3</h1></center>
## Definitions
- Packet size: length of a packet (bits or bytes), incl. header and data
- **Bandwidth**: for a single link, amount of data it can transmit per unit time
- **Propagation delay:** time needed to move one bit across (second)
	- imposed by communication medium; *depends* on link length
- **Transmission delay:** Time from first bit@sender to last bit@sender
	- determined by link bandwidth and packet size
- **Queuing delay:** Time that a packet waits for transmission
	- determined by contention for the link (variable)
- **Total packet delay**: time from first bit@sender to last bit@receiver

## Delay
We can compute total packet delay with the following formula:

$d_p$ = propagation delay
$d_q$ = queuing delay
$d_t$ = transmission delay

$d = d_p + d_q +d_t$

The delay is modeled in the image below.
![[Pasted image 20221005004852.png]]

## Application-layer communication
The internet applications reside on multiple endpoints. We use **addresses** to identify the communicating endpoints.

So, each of these endpoints is assigned an **Internet Protocol (IP) address**.
- IPv4: 128.6.24.78
- IPv6: 2001:4000:A000:C000:6000:B001:412A:8000