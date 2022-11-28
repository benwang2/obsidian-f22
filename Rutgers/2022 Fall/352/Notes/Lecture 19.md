---
title: Lecture Notes 19
course: CS_352
date: 2022-11-18
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 19</h1></center>

## Network Layer
The network layer's main function is to move data from the sending endpoint to the receiving endpoint.

On the sending endpoint, data is encapsulated into **datagrams**, which the receiving endpoint delivers to the transport layer.

The network layer is difficult to evolve because it **runs in every router**. The iteration of the network layer is deeply ingrained in our ecosystem.

### Key functions
**Forwarding** - move packets from router's input to appropriate router output.

An analogy for forwarding is taking a road trip, specifically getting through a single interchange.

**Routing** - determine route taken by packets from source to destination. Utilizes routing algorithms.

An analogy 