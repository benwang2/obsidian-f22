---
title: Lecture Notes 11
course: CS_352
date: 2022-10-14
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 11</h1></center>

## Error Detection
We implement error detection because the network provides no guarantees for correctness.

We can use a computing function to verify that the packet has be transmitted correctly. This function is called the **checksum** and it must:
- be easy to compute
- change if the packet changes
- be easy to verify

#checksum

### Checksum
| sender                                                   | receiver                                                                  |
| -------------------------------------------------------- | ------------------------------------------------------------------------- |
| treat segment contents as sequences of 16-bit integers   | compute checksum of received segment, inclduing checksum in packet itself |
| check: addition (1's complement sum) of segment contents | check if resulting checksum is 0                                          |
| sender puts checksum value into UDP/TCP checksum field   | NO - an error is detected                                                 |
|                                                          | YES - assume no error                                                     |


C