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

An analogy for **forwarding** is taking a road trip, specifically getting through a single interchange.

**Routing** - determine route taken by packets from source to destination. Utilizes routing algorithms.

The process of planning a trip from source to destination is called **routing.**

### Planes
There are two planes:
- data plane
- control plane

#### Data plane
The data plane performs **forwarding**. Its' function is locally implemented. It determines how datagrams arriving on the router input port is forwarded to the router output port.

#### Control plane
The control plane performs **routing** and follows network-wide logic. It determines how datagrams are routed along end-to-end path from source to destination endpoint.

There are two common control-plane approaches:
- **distributed routing** - algorithms running on each router
- **centralized routing** - algorithm running on a logically centralized server

## Addressing
Internet addresses allow endpoints to *locate each other* but they do not identify endpoints.

The internet addresses only determine how to move a packet.

Network layer addresses are **designed** to help routers perform the forwarding and routing functions **efficiently**.

### IPv4
An IPv4 address is 32 bits long and it identifies a network interface. 

The IPv4 address corresponds to a point of attachment of an endpoint to a network, but it is NOT an identifier for the endpoint. If the endpoint relocates, the IP changes.

IPv4 addresses are written in **dotted quad notation**, where each byte is written in decimal in order, seperated by dots.

Example:
| 10000000 | 11000011 | 00000001 | 01010000 |
| -------- | -------- | -------- | -------- |
| 128      | 195      | 1        | 80         |

IP addresses can be grouped based on a **shared prefix on a specified length**.

So the two addresses below:
- 128.95.1.80
- 128.95.1.4
Share the prefix of length 24: $128.95.1$ but have different suffixes of bit length.

For each address, the prefix corresponds to the network component and the suffix to an **endpoint (host) component** of the address.

### Scaling
IP addresses use hierarchy to scale routing. For example, endpoints within Busch campus share a prefix of some length, but each endpoint has a different suffix.

Prefixes reduce the amount of information needed to forward packets over the internet.

IP prefixes are like **zip codes** and they allow for IP addresses to be delegated from one network to another.