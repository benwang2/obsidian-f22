---
title: Lecture Notes 22
course: CS_352
date: 2022-12-02
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 22</h1></center>
## Internet Control Message Protocol (ICMP)

>*ICMP is a protocol for **troubleshooting** and diagnostics and it works over IP.*

### Traceroute
Traceroute is a tool records the router-level path taken by packets. It cleverly uses the IP time-to-live field to identify all the routers in the path.

When a router receives an IP packet, it decrements the TTL field by 1. When the TTL is decreased by one, the IP packet is discarded. This is a failsafe mechanism to ensure packets don't take up too much memory in the network. 

The traceroute algorithm works as follows:
- Send a packet with TTL = n to IP
- Packet is received by router, then TTL is decremented by 1
- If TTL is now 0, then respond to source with TTL exceeded
- Otherwise, forward to next router
- When source receives TTL exceeded, n = n+1 and jump back to first step
- If source receives ICMP reply, we know the destination is reachable and learned all routers in  the path

## Network Address Translation
``