---
title: Lecture Notes 4
course: CS_352
date: 2022/09/13
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 4</h1></center>

## Application Architectures
### Client-server architecture
#### Server
Always-on endpoint that provides a "service" to the world. It is typically a permanent IP address. The sever may have compute clusters to scale to many users.

#### Clients
A client acts as a "customer" of the server - it is serviced by the server and may be intermittently connected. Clients might also have dynamic IP addresses. Typically, clients don't communicate with other clients.

### Peer-to-peer architecture
Peers are intermittently connected hosts that directly speak to eachothers. Eahc peer is a client. With this architecture, there is little-to-no reliance on always-up servers.

Many applications today use a hybrid model (between p2p and client-server).

For example, WebRTC, Google Meet, and Facebook Messenger.

#p2p
#client-server

## Domain Name System
Each device can be reached by accessing it's IP address. However, an IP address has 12 digits on address, whereas the average brain can remember 7 digits for a few names.

In an expensive network with many different services and names, we use alphanumeric names to refer to hosts.

These are called **host names** or **domain names**