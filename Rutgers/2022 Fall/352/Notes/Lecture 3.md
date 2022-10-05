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

Different applications communicate on different **port numbers**, using **sockets**.

**Sockets** are an abstraction of the Internet for applications. In other words, applications utilize sockets to connect to the internet.

## Questions
1. Suppose two endpoints are communicating with each other. Suppose: 
   (1) It takes 50 milliseconds for a single bit to move from the source to the destination over the network path between them. 
   (2) The transmission delay to push a single packet over this path is 25 milliseconds.
   (3) The packet waits in a queue along the path for 10 milliseconds.
   Then, the total delay experienced by the packet (from the start of transmission at the source up to finishing reception of the complete packet at the destination) is how many milliseconds?

85ms

2. Choose the most appropriate answer. What API does application software use to communicate with another endpoint in the Internet?
   <input type="radio"> Docket
   <input type="radio"> Sprocket
   <input type="radio"> Rocket
   <input type="radio" checked> Socket
   
3. What problem does the domain name system solve?
```
This DNS resolves IP addresses to names so people can more easily remember destinations.
```