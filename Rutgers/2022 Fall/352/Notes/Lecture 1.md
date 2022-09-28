---
title: Lecture Notes X
course: CS 352
date: 2022/09/06
tags: "Lecture Notes"
---

# Lecture 1
## Networks
### Single link multiple acccess network
-   send bits of data in packets or frames
-   every endpoint as a link level address ([[MAC address]])
-   there are physical limits on power distance over which info travels over a single link
-   all packets have a destination address on them  

**How can you carry information between different endpoints?**
Use a processes called [[encoding]] and [[decoding]], which allows us to transmit information from endpoint to endpoint.

[[medium access control problem]]

**TCP** and **UDP** protocols are used for detecting and correcting errors. 
  
### Multi link network
-   Routers relay information from multiple links
-   There are links to the router and a link to the ISP
-   The routing problem is the question “how can we determine where to send packets”

Networks give no guarantees, but packets may be lost, corrupted, reordered on the way to the destination (best effort delivery).

With [[best effort delivery]], the network is simple to build
-   reliability not required
-   dont have to implement any performance guarantees
-   dont need to maintain packet ordering
-   almost any medium can deliver individual packets ([RFC 1149](https://www.rfc-editor.org/rfc/rfc1149): ip datagrams overavian carriers)
    

  

With such a simple network model, the early internet thrived because it was easy to engineer

  

Endpoints provide guarantees to applications, not the network itself. Transport software on the endpoint oversees the implementing guarantees on top of unreliable networks.

  

How do we solve the reliable data delivery problem?

This problem is solved by transport software.

  

For some applications, ordered delivery is required.  
  

Transport software also resolves resource allegation (congestion control).

If a link is overloaded, it might have unintended behavior.

  

Congestion control algorithms are solved by the device. (Part of sw/hw stack)

  

Transmitting packets when network resources are scarce (packet scheduling problem)

related to the buffer management problem

  

Link - communication links for transmission

Host/endpoint - compute running applications of end user

outer - computer for routing packets from input link to another output link

Network - a group of hosts, links, routers capable of sending packets among its members

  
**