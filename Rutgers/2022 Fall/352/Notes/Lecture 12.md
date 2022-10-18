---
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
Sending one packet at a time causes data transfer rate to be limited by **time** between endpoints rather than **bandwidth**.

## Pipelined Reliability
**Data in flight:** data that has been sent, but sender hasn't yet received ACKS from the receiver.

### Key ideas
- New packets can be sent at the same time as older ones still in flight.
- New packets sent at the same time as ACKs are returning.

If there are N packets in flight, **throughput** improves by N times.

#throughput

### Sliding Window
The sender and receiver use a sliding window algorithm to more effectively transmit data.

- **Window**: sequence numbers of in-flight data
- **Window size**: the amount of in-flight data (unACKed)

#### Sender
The sender utilizes a sliding window to keep more data in flight at once.

Sequence numbers restart from 0 after they've exceeded the space on the header.
Upon receiving an ACK for $i$, the sender can transmit the sequence $i+n$ where $n$ is the size of the sliding window.

#### Receiver
Between the sender and receiver, window of in-flight packets can look different.

The receiver only accepts sequence numbers allowed by the current receiver window. Any sequence numbers outside of this window will be dropped.

#### Summary
Using the sliding window algorithm, the sender and receiver can keep several packets of in-flight data.

The windows slide forward as packets are ACKed (at receiver) and ACKs are received (at sender).

### Identifying dropped packets
The sendercan infer which data was received sucessfully using the ACK sequence numbers.