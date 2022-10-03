---
title: Lecture Notes 2
course: CS_352
date: 2022/09/09
tags: 
- lectureNotes
- CS_352
---

# Lecture 2
## Transmitting data
Machines communicate exclusively in binary, however the data that needs to be transmitted is often a much more complex data type than binary.

This is the **encoding and decoding problem**. The complex data types can be encoded and decoded on different entities in the network.

### Physical transmission on a single link
Physical signaling (light, AC, voltages) are often analog forms of transmission.

BIts are converted to signals through **modulation** of physical characteristics of signals. This is called **encoding**.

For example, one might modulate the voltage to achieve a certain pattern in the signals sent.

The receiving endpoint converts the signals back to digital by **decoding** physical signals.

There are three different types of modulation
- amplitude modulation
- frequency modulation
- phase modulation
