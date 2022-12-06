---
title: Lecture Notes 23
course: CS_352
date: 2022-12-06
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 23</h1></center>

## Control plane
The control plane is **distributed** throughout routers. Components in every router interact with other components to produce a routing outcome. 

Data plane performs per-packet processing, moving packet from input port to output port.

Routing algorithms work over an abstract representation of the network, called **the graph abstraction**.

Each router is a **node** in a graph and each link is an **edge** in the graph. Additionally, edges have **weights** (called **link metrics**) which is set by netadmin.

The cost of an edge is defined as **c(x, y)** and the cost of a path is the **sum of the edge costs.**

Each node should determine the least cost path to every other node.