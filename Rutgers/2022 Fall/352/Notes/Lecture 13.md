---
title: Lecture Notes 13
course: CS_352
date: 2022-10-25
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 13</h1></center>

## Handling dropped packets

```mermaid
flowchart TD 
	ROOT(ACK packets after drop?) -- NO --> NO
	NO(Go-back-N)
	ROOT(ACK packets after drop?) -- YES --> YES
	YES(Selective Repeat, check # on ACK) --> CUMULATIVE(Cumulative ACK)
	YES --> SELECTIVE(Selective ACK)
```

### Sliding Window with Go Back N
When a receiver notices missing data, it simply **discards** all data with greater sequence numbers.

The sender will eventually time out (RTO) and retransmit data in sending window.

The main benefit of Go back N is that it can recover from erroneous or missing packets. However, it is very wasteful.

If any errors occur, the sender spends time and network retransmitting data 

![[Pasted image 20221107202526.png]]

