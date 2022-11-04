---
title: Lecture Notes 352 
course: CS_352
date: 2022-11-04
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 17</h1></center>

## Congestion Window
The sender maintains an estimate of the amount of in-flight data needed to keep the pipe full without congesting it. This estimate is called the **congestion window (cwnd)**. #congestion_control #congestion_window

The larger the congestion window, the higher the #throughput.
As a TCP sender, the window size is the minimum of the congestion window and the receiver advertised window in order to respect whichever peer is the slowest.

## Congestion Avoidance
#### TCP New Reno
Follow a "slow start" approach, with an additive increase.

There is exponential growth for sending packets. When packet loss occurs at sending rate = $n$, reset the packet sending rate to 0, start growth again. Repeat this until sending rate = $n-1$, then there is an additive increase. This algorithm is repeated.

This method of adjusting is just one of many **congestion avoidance** methods.

#### TCP BBR
