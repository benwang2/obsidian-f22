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

#encoding, #decoding

### Physical transmission on a single link
Physical signaling (light, AC, voltages) are often analog forms of transmission.

BIts are converted to signals through **modulation** of physical characteristics of signals. This is called **encoding**.

For example, one might modulate the voltage to achieve a certain pattern in the signals sent.

The receiving endpoint converts the signals back to digital by **decoding** physical signals.

There are three different types of modulation
- amplitude modulation
![[Pasted image 20221003163942.png]]
- frequency modulation
![[Pasted image 20221003164011.png]]
- phase modulation
![[Pasted image 20221003164128.png]]

#modulation

## Switching
The term **switching** is used to denote physically moving data from one linke to another.

There are several different **switching schemes**.
- Circuit switching
- Message switching
- Packet switching

#switching
### Circuit Switching
With circuit switching, the full path of connected links are allocated to the connection.

An example of this is a telephone network.

This method of switching follows the certain steps.
1. **Setup:** Control message sets up path from origin to destination
2. Accept signal informs source that data transmission may proceed
3. **Data transmission** begins
4. Entire path remains allocated to the transmission (whether used or not)
5. Whether transmission is complete, source releases the circuit

![[Pasted image 20221003172520.png | center]]


#circuit_switching
### Message Switching
With message switching, each message is addressed to a destination. The message is addressed using the **header**.

The **header** includes metadata that denotes how to process a message, like a *destination address*

The message "hops" from node to node through a network, **while allocating only one link at a time**, as opposed to circuit switching where all links are reserved at the same time (regardless of use).

When the entire message is received at a router, the next step and link in its journey are selected (**routing**). If the selected link is busy, the message waits in a **queue** until the link is free.

An analogy for this is a postal service.

![[Pasted image 20221003172506.png]]

#message_switching
### Packet Switching
With packet switching, messages are split into smaller pieces called **packets**. Packets have the following properties:
- max length
- numbered and addressed
- sent through network one at a time

![[Pasted image 20221003173126.png]]
#packet_switching

### Store and forward switching
With store and forward switching, the router waits for all bits to arrive on incoming link before sending the frist bit of the message on the outgoing link.

Alternatively, **cut-through** switching sends bits *as they arrive*.

#store_and_forward
#cut-through

### Pipelining
With pipelining, different parts of a messsage concurrently transmitted over different links. Pipelining provides a higher utilization of link resources.

It's similar to computing an operation using multithreading.

#pipelining

### Comparisons
Circuit switching incurs an initial delay to set up the path, but packet and message switching can start transmitting data immediately.

Packet switching doesn't reserver resources for the conversation, but circuit switching does (admission control). Packet switching makes resource reservation decisions per packet.

The fewer guarantees, the easier the network is to build. Therefore, a telephone network is both more reliable and more difficult to build.

#### Total delay
For data that is of small size and to be transmitted quickly, circuit switching is better than packet switching.

For data that is a long, continuous stream, packet switching is better than circuit switching.

#### Overhead
If messages are bigger than typical packets then packet switching is better than message switching.

## Layering and Protocols

### Software / Hardware organization
The network is constructed in layers, each providing a different function to the network.
- **Application**: useful user-level functions
- **Transport**: provide guarantees to apps
- **Network**: best-effort global packet delivery
- **Link**: best-effort local packet delivery

Communication functions are broken up and "stacked". Each layer is dependent on the layer beneath it, and each layer supports the layer above it.

The interfaces between 

 

 