---
title: Lecture Notes 20
course: CS_352
date: 2022-11-29
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 20</h1></center>

## Router Architecture
### Input port functions
**Route lookup** is the high-speed lookup of which output port the packet is destined to. The goal of the router is to complete the process at the line rate.

If packets are arriving too fast for the switching fabric to send them to the output port, packets may wait in **per-output-port queues**.

#### Route lookup
Packet forwarding is based on the destination IP address on the packet. When a router receives and parses a packet, it extracts the destination IP address from the packet and does the lookup.