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

### Identifying dropped packets
```mermaid
flowchart TD 
	ROOT(ACK packets after drop?) -- YES --> YES
	ROOT(ACK packets after drop?) -- NO --> NO
	NO(Go-back-N)
	YES(Selective Repeat)
	
```
