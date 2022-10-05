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

We can compute total packet delay with the following formula:

$d_p$ = propagation delay
$d_q$ = queuing delay
$d_t$ = transmission delay

$d = d_p + d_q +d_t$
