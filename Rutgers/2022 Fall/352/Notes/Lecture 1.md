---
title: Lecture Notes 1
course: CS_352
date: 2022/09/06
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 1</h1></center>
## Network
A network is a carrier of information between two or more entities.

Entities may be **hosts** or **endpoints**. Some examples are:
- cell phone
- laptop
- wifi printer
- router

#hosts, #endpoints

The interconnection between entities is any physical medium capable of carrying information: **links**
- wireless links: cellular 4G/5G, wifi 802.11, bluetooth, satellite
- wired links: copper wire, lasers over optic fiber, coax cables

#links

### Single Link Multiple Access Network
In a single link multiple access network, data is sent in **packets** or **frames**.

A **packet** is a unit of data transmission.

Networks differentiate receivers using a link level address, called a **MAC address**

On a link, digital data must be converted to physical signals over medium, using encoding and decoding.

Control over information transmission is called medium access control.

Follows a "peer-to-peer" model, where each device is reaches another device with a *single link*.

#mac_address
#packets
#medium_access_control

### Multi-link Network
In a multi-link network, routers relay data across multiple links to it's destination endpoint.

There are links from devices to devices, devices to routers, and routers to the ISP.

In a multi-link network, we encounter the **routing problem** which asks the question: "How can we determine where to send packets"?

#routing-problem
#multi-link
#isp

## Data Transmission
The network gives no guarantees, meaning that data can be lost, corrupted, or reordered on the way to the destination. This is called **best effort delivery**

Best effort delivery makes the network trivial to build because:
- reliability not required
- don't have to guarantee performance
- don't have to maintain packet ordering
- nearly any medium can deliver individual packets [RFC 1149: A Standard for the Transmission of IP Datagrams on Avian Carriers](https://datatracker.ietf.org/doc/html/rfc1149)

#best_effort_delivery

Using best effort delivery, the early internet thrived because it was easy to engineer.

#### Endpoints
The endpoint can be considered part of the software / hardware stack in the modular design of a network.

Due to best effort delivery, it's the responsiblity of the **endpoint** to provide guarantees to applications.

**Transport software** on the endpoint oversees the implementing guarantees on top of unreliable networks. Transport software solves the **reliable data delivery problem**.

Transport software resolves resource allegation (**congestion control**).

The device solves the **congestion control problem**.

The **packet scheduling problem** asks the question: "how do we transmit packets when network resources are scarce?" Packet scheduling determines which packet to transmit over a constrained network link and when.

It is related to the **buffer management problem**. 

#reliable_data_delivery
#congestion_control
#resource_allegation

# Questions
1. Your laptop is an example of a/an
<input type="radio"> router
<input type="radio"> link
<input type="radio" > network
<input type="radio" checked> endpoint

2. What does "best effort" mean in the context of the Internet?
<input type="radio"> The network will carry messages in order.
<input type="radio"> The network maintains strict guarantees on the quality of service received.
<input type="radio"> The network delivers data reliably.
<input type="radio" checked> The network does not provide any guarantees for data it carries.