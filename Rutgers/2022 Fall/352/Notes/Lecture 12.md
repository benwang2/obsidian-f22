--
title: Lecture Notes 12
course: CS_352
date: 2022-10-18
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 12</h1></center>

## Receive Timeout (RTO)
A good RTO predicts the round-trip time (RTT) between sender and receiver. 

If an ACK hasn't been returned within our estimated RTT, the packet was likely dropped. RTT can be measured directly at sender - no receiver or router help is needed. 

If the receiver determines the packet was dropped, the sender **retransmits** the packet.

#rto #retransmit #timeout

### Packet Duplication
If ACKs are delayed beyond the RTO, the sender might retransmit the same data. We can resolve this issue by adding an identification to each packet to help distinguish between adjacent transmissions.

These identifiers are known as **sequence numbers**.

A sequence number helps disambiguate a fresh transmission from a retransmission.

## Stop-and-Wait Reliability

The sender sends a single packet. then waits for an ACK. If an ACK is not received until RTO, then retransmit the packet.

Disambiguate duplicate vs. fresh packets using sequence numbers that change on "adjacent" packets.

### Efficiency problem
