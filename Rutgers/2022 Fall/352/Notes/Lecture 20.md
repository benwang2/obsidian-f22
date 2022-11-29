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

If packets are arriving too fast for the switching fabric to sendNumber of entries them to the output port, packets may wait in **per-output-port queues**.

#### Route lookup
Packet forwarding is based on the destination IP address on the packet. When a router receives and parses a packet, it extracts the destination IP address from the packet and does the lookup.

**Number of entries** in the forwarding table is significant - it must fit into the router memory and be efficient.

Number of table entries in a router is proportional to number of prefixes, not endpoints. Therefore, we do not have to store data for millions of endpoints.

However, with destination-IP-based forwarding, there are consequences:
- forwarding behavior is independent of source (bad actors can exploit system)
- forwarding behavior is independent of application (web traffic vs file download vs video)
- IP-based packet processing baked into router hardware so evolving IP protocol is just as challenging as evolving routers
 
### Output port functions
The output port receives from the switching fabric into the queues, which is transmitted to the link layer, then to line termination. Finally, it is transmitted from the output link.

Most routers have the bulk of their **packet buffers** in their input ports, stored in reverse order.

**Scheduling:** which among the waiting packets gets to be transmitted out the link?
**Buffer management**: which among the packets arriving from the fabric gets space in the packet buffer.

### Switching Fabrics
The goal of fabric is to ferry as many packets as possible from input to output ports as quickly as possible.

#### Memory
Input port writes packets into shared memory and output port reads the packet when output link ready to transmit

#### Bus
single shared channel to move data from input to output port. easy to build buses; technology is quite mature

#### Crossbar
each input port has a physical data path to every output port. *Switch* over at the cross-over points turns on to connect pairs of ports

crossbars can get expensive as the number of ports grow (N^2 connections for N ports). MGR uses a crossbar and schedules (in, out) port pairs.

### Nonblocking fabrics
High-speed switching fabrics are designed to be nonblocking:
- if an output port is "available", an input port can always transmit to it without being blocked by the switching fabric itself
- nontrivial to achieve

Crossbars are nonblocking by design and shared memory can be designed to be nonblocking if the memory access is fast enough.

With a nonblocking fabric, queues aren't formed due to the switching fabric and there are no queues due to inefficiencies at the input port or switching fabric.

Queues form as a result of contention for the output port. They are unavoidable given the route.

