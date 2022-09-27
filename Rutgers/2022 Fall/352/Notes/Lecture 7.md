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

[[user agent]]

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

### Observations
Mail servers are the **infrastructure** for email functionality and can act as both the client or the server based on the context.

SMTP is **push-based**, meaning that everything is reliant on info being *pushed* from client to server.

[[push-based]]

### Mail Response Codes
| code | description              |
| ---- | ------------------------ |
| 220  | Service ready            |
| 250  | Request command complete |
| 354  | Start mail input         |
| 421  | Service not available    |
| 500  | Unrecognized command     |


### Message Format
The message format for SMTP was standardized in [RFC 822](https://learn.microsoft.com/en-us/previous-versions/office/developer/exchange-server-2010/aa493918(v=exchg.140)). It as constructed as such:
- Header lines (to, from, subject)
- Body (message, ascii characters only)

There is a blank space between the header and the body when the message is transmitted. This format was stored on the **mail server**.

#### MIME
Multipurpose Internet mail extension ([MIME](https://en.wikipedia.org/wiki/MIME)) was established in [RFC 2045](https://www.rfc-editor.org/rfc/rfc2045) and [RFC 2046](https://www.rfc-editor.org/rfc/rfc2046)

Additional headers in the data header specify the MIME content type and version. The message can have many parts.

[[MIME]]

## Mail Access Protocols
### Access protocols
Whereas SMTP is focused on pushing data, the mail access protocols are focused on pulling data.
- POP: Post Office Protocol ([RFC 1939](https://www.rfc-editor.org/rfc/rfc1939))
- IMAP: Internet Mail Access Protocol ([RFC 1730](https://www.rfc-editor.org/rfc/rfc1730))
- HTTP: Gmail, Outlook, etc.

[[POP]], [[IMAP]], [[HTTP]]
### Web-based email (HTTP)
Web-based emails connect to mail servers via web browser. Browsers work in HTTP requests, whereas email servers use SMTP. The browser makes a HTTP request to the HTTP server, which then communicates to the mail server in SMTP.

In some configurations, the HTTP server and SMTP server can be on the same machine.

### SMTP vs. HTTP
| HTTP                               | SMTP                                       |
| ---------------------------------- | ------------------------------------------ |
| pull                               | push                                       |
| 1:1 object to message              | multiple objects sent in multipart message |
| can put non-ascii data in response | need ascii-based encoding (base64)

Both protocols have ASCII command/response interactions and status codes.

[[base64]]
[[ascii]]

