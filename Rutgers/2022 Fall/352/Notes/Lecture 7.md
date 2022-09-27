---
title: Lecture Notes 7
course: CS_352
date: 2022-09-27
tags: "Lecture Notes"
---

# Lecture 7
## Simple Mail Transfer Protocol
Simple Mail Transfer Protocol (SMTP ) allosw us to send and receive messages fr ka aj, server.

[[smtp]]
[[mail server]]

### Components
SMTP is composed of 3 main components:
- user agents
- mail server
- smtp protocol

#### User Agent
A user agent is the client a user may use to access their mailbox. This may be an application like Outlook or Apple Mail. It could also be a web client, like Gmail or Yahoo Mail.

#### Mail Server
The mail server contains a **mailbox** for incoming messages for a user. It also queues outgoing messages from a user. The sender's mail server makes a connection to the receiver's mail server on port 25.

#### SMTP
The SMTP protocol is used to send messages from client to server. The client (either a user agent or sending mail server) sends the message. The server is the *receiving* mail server.

### Scenario
1. **User 1** composes a message to **User 2**
2. **User 1**'s client is sent to the mail server and the message is placed in outgoing queue
3. Client side of SMTP opens TCP connection with **User 2**'s mail server.
4. SMTP client sends **User 1** message over TCP connection
5. **User 2**'s mail server places inbound message in mailbox
6. **User 2** invokes client to read message

### Sample Interaction
