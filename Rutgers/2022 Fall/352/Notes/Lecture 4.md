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

These are called **host names** or **domain names**, which the DNS resolves to an IP address.

The DNS uses a **directory** to map alphanumeric host names to binary IP addresses, which is called **Address Resolution**.

### Types of Directories
A directory maps a name to an address. There are different designs of directories.
| Simplstic | Scalable distributed   |
| --------- | ---------------------- |
| Central   | Hierarchical namespace |
| Flooding  | Flat name space        | 
| Broadcast |                        |

### Simple DNS
In the early days of internet, every endpoint had a local directory stored at /etc/hosts.txt.

When an endpoint changed addresses, the endpoint would query the DNS server with a 4-component tuple.

The four components of the tuple were ($IP_A$, $Port_A$, $IP_B$, $Port_B$), where $IP_A$ and $Port_A$ described the source address and port.
$IP_B$ and $Port_B$ described the destination adress and port.

By distributing data throughout a hierarchy, the DNS is able to scale well. The hierarchy also has other benefits including but not limited to:
- better security (have to hack many servers instead of one)
- fault tolerance
- improved performance

Different DNS servers service resolve domain names for its own extension. For example, there are DNS servers for .com, .org, .edu, and so on.

When a domain name becomes too saturated, we can add additional DNS servers to help resolve names to addresses.

### DNS Protocol
The DNS protocol is used in the client-server application and will always occupy port 53 on the server.

There are two types of messages - queries and responses.

##### Query
A query is a request made to the DNS server, which asks for an IP address given a domain name.

A query has an OPCODE of 0x0.

##### Response
The DNS server responds with a resolved IP address for the domain name provided.

#### Message Format
Each message is sent with a message header. The message header includes...
- QR: QR=0 if Query, QR=1 if response
- OPCODE = 0
- ID: 16 bit # to identify query and respond with
- Flags
	- Authoritative answer?
	- Recursion desired
	- Recursion available
	- Reply is authoritative

The header is 12 bytes in size.

The body contains the following:
- Name, type fields
- Resource records
- Records for authoritative servers
- Additional "helpful" info

All of these may return a variable amount of data.

#### Actions
When a client wants to know an IP address for a host name, it sends a query to the authoritative name server.

In the situation that the authoritative name server doesn't have the mapping, the name server will forwards the request to the root server.

The root server will resolve the IP address for the authoritative name server, then respond to the originating name server.

The request works its way down from the root server until it reaches a naem server with a mapping for the requested domain name.

```mermaid
flowchart
local["Local DNS Server"] -> root["Root DNS Server"]
```
