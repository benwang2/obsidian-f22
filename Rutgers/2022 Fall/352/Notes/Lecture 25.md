---
title: Lecture Notes 25
course: CS_352
date: 2022-12-19
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 25</h1></center>

## Computing the Forwarding table
- Suppose a router in AS1 to forward a packet destined to external prefix X.
- How is the forwarding table entry for X at 1d computed?
- How is the forwarding table entry for X at 1c computed?

### eBGP and iBGP announcements
- AS2 router 2c receives path announcements AS3,X (via **eBGP**) from router 3a
- Based on AS2 import policy, AS2 router 2c imports and selects path AS3,X, propagates (via iBGP) to all AS2 routers
- Based on AS2 export policy, AS2 router 2a announces (via eBGP) path AS2, AS3,X to AS1 router 1c

A router may learn about **multiple** paths to a destination:
- AS1 gateway router 1c learns path AS2, AS3, X from 2a (next hop 2a)
- AS1 gateway router 1c learns path AS3, X from 3a (next hop 3a)
- Through BGP route selection process, AS1 gateway router 1c chooses path AS3,X, and announces path within AS1 via iBGP

### Setting forwarding table entries
...

### Inter-domain routing
- **Federation** and **scale** introduce new requirements for routing on the Internet
- **BGP** is the protocol that handles Internet routing
- **Path vector**: exchange paths to a destination with attributes
- **Policy-based** import of routes, route selection, and export

## Quality of service
A **best effort** Internet architecture does not offerany guarantees on delay, bandwidth, and loss
- network may drop, reorder, corrupt packets
- network may treat traffic randomly regardless of their "importance"

Meanwhile, certain applications may require special treatment and guarantees
- voice over IP require strict delay guarantees
- HD video requires reasonable minimum bandwidth
- remote surgery with 3D-vision requires strict sync and latenccy

How can we provide quality of service for applications?



### Shortcomings of best effort

With best effort, **contention** is still an issue.
Because resource contention occurs in the **core** of the network, congestion control will react, but may be too little and too  late.
- Congestion control can not prevent packet drops "now" (only after the fact)
- Congestion  control won't prevent high-sending-rate flows from inflicting large delays or recurring drops

### Approaches to resolving quality of service
#### Provision more capacity
- ISPs may deploy enough capacity such that contention no longer occurs (low complexity solution)
- This approach has high costs (e.g. bandwidth, hardware)
- Furthermore, how do we estimate the required bandwidth?
	- Need to estimate demand over time?
	- Network operators can do this quite well
	- Must handle exceptional circumstances: pandemics, superbowl

#### Classes of service
With classes of service, the network treats different traffic differently, also known as **traffic differentiation**. An excellent analogy used is: liens at an airport (first class vs economy).

Traffic is partitioned into  classes and offer service guarantees **per class** and **across classes**
- classes may be indicated using IP type of service header bits
- classes may be inferred from IP & transport headers (e.g. src/dst/ports)

**Packet classification**: assigning packets to classes

## Kinds of Service Guarantees

### Strict prioritization
- Suppose a 1Mbps interactive flow and an HTTP connection share a 1.5 Mbps link
- A network operator might choose to prioritize interactive app strictly over the HTTP flow

### Rate limiting
- What if a flow doesn't respect its allocation?
	- If a conference call goes beyond 1Mbit/s, what do we do?
- An operator may limit a flow to a certain max rate
- **Isolation**: HTTP should not be impacted by the conference call

### Weighted fair sharing
In weighted fair sharing, an operator might want to partition the link's rate **C** into separate allocations for each class. Partitions may have **weights w**.

Class $i$ gets the illusion of traversing logical link rate $w_i * C / \sum_j w_j$

- Customary to think of different classes as belonging to different **queues**
- For this reason, weighted fair sharing is also called **weighted fair queuing (WFQ)**
- Each queue is first-in-first-out (FIFO)
- Link multiplexes among these queues
- Intuitively, packets of one queue should not influence behavior of other queues
- Fair queuing is also a form of isolation across traffic classes
- Other classes can use unused capacity from other classes
- WFQ is **work-conserving**: a router implementing WFQ allows other classes to use unused capacity
- Work conservation makes WFQ different from rate limits applied sepearately to each class
- Class $i$'s usage can exceed $w_i * C / \sum_j w_j$
- 