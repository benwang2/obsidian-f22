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