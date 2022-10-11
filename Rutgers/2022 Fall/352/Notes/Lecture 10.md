---
title: Lecture Notes 10
course: CS_352
date: YYYY/MM/DD
tags: 
- lectureNotes
- CS_XXX
---

<center><h1>Lecture 10</h1></center>

# Transport Layer Protocols
## User Datagram Protocol (UDP)
UDP functions as a simple wrapper around packet delivery. UDP provides a **best effort service** and as a result, UDP segments may be lost, corrupted, or reordered.

UDP is **connectionless**, meaning that each UDP segment is handled independently of others (no memory acros)

## Transmission Control Protocol (TCP)
TCP provides delivery guarantees for ordering, efficiency, and fair bandwidth use.

#tcp #udp
# Multiplexing
Multiplexing is a way of sending multiple signals or streams of information over a communications link at the same time in the form of a single, complex signal.

#multiplexing
# Demultiplexing
Demultiplexing is the process of reconverting a signal containing multiple analog or digital signal streams back into the original separate and unrelated signals

Each packet has a source IP and destination IP, with the source port and destination port. The transport layer utilizes demultiplexing to obtain this information and deliver the packet to its destination effectively. 

When a packet is received by a device, the machine does a lookup on a table contained by the machine. Ports are mapped in a table, and the machine does a **connection lookup** to find the correct destination.

Demultiplexing allows for the machine to receive input from multiple sources at once, and then direct them to their respective port.

# Sockets
## TCP Sockets
**TCP sockets** are used to received and send packets. These sockets have the following components to identify them:
- Source IP
- Destination IP
- Source port
- Destination port

### States
TCP sockets have different states and types:
- **listening**
- **connected**

A socket that is **listening** (bound but unconnected) has no specific source that it is associated with, but it actively listening for inbound traffic.

A socket that is connected (**established**) has information containing the source and the destination address and are ready to communicate. In this situation, a socket will give a **csockid**.

### Demultiplexing TCP
When a TCP packet is received, the operating system:
1. looks up a table of existing connections using 4-tuple, then sends to the established socket if possible
2. if failed to find socket, look up list of listening connections with the destination IP and port. If this succeeds, send to the corresponding port
3. if both steps have failed, send an error to the client

## UDP Sockets
**UDP sockets**, on the other hand only contain a destination IP and a destination port. So, all packets directed to a UDP socket will end up in one destination. There is no memory of which device is being communicated with. These sockets are often shared across many sources.

### UDP Demultiplexing
When a UDP packet comes in, the operating system:
1. Look up table of listening UDP sockets using (destination IP, destination port)
	- If success, send packet to corresponding socket
2. If fails, send an error to the client



#demultiplexing