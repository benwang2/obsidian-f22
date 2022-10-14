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
A checksum is the 16-bit one's complement of the one's complement sum of a pseudo hedaer of information from the IP header, the UDP header, and the data, padded with zero octets at the end to make a multiple of two octets.

The pseudo header conceptually prefixed to the UDP header contains the source address, the destination address, the protocol, and the UDP length.


| sender                                                   | receiver                                                                  |
| -------------------------------------------------------- | ------------------------------------------------------------------------- |
| treat segment contents as sequences of 16-bit integers   | compute checksum of received segment, inclduing checksum in packet itself |
| check: addition (1's complement sum) of segment contents | check if resulting checksum is 0                                          |
| sender puts checksum value into UDP/TCP checksum field   | NO - an error is detected                                                 |
|                                                          | YES - assume no error                                                     |

Checksums are not the end-all-be-all; they don't detect all bit errors.
*analogy*: "you can't assume the package hasn't been meddled with if it's weight matches the one on the stamp"
The checksum is an effective and lightweight method to validate packet accuracy

[RFC 768](https://www.rfc-editor.org/rfc/rfc768)
