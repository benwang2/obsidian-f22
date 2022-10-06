---
title: Lecture Notes X
course: CS_XXX
date: YYYY/MM/DD
tags: 
- lectureNotes
- CS_XXX
---

<center><h1>Lecture 5</h1></center>

## DNS Resource Records
DNS is a distributed database that stores **resource records (RRs**)

Each resource record contains a class, type, name, value, and time to live.

### Types of Records
Type=A
- **name** is hostname
- **value** is IPv4 address

Type=AAAA
- **name** is hostname
- **value** is **IPv6** address

Type=NS
- **name** is domain
- **value** is hostname of authoritative name server for this domain
- sometimes see SOA record

Type=CNAME
- **name** is alias for some "canonical" (the real) name (ibm.com is ibm.com.cs186.net)
- **value** is canonical name

Type=MX
- **value** is name of mailserver associated with name

### Example
An example DNS record example might look like the following:

A resource record in response to query
| NAME    | design.cs.rutgers.edu |
| ------- | --------------------- |
| TYPE    | A                     |
| CLASS   | IN                    |
| TTL     | 1 day (86400s)        |
| ADDRESS | 192.26.92.30          |

Records for authoritative servers information about nameserver
| NAME    | cs.rutgers.edu      |
| ------- | ------------------- |
| TYPE    | NS                  |
| CLASS   | IN                  |
| TTL     | 1 day (86400s)      |
| NSDNAME | ns-lcsr.rutgers.edu |

## HTTP
HTTP stands for "HyperText Transfer Protocol". Every web page is made up of many **objects**.

An object can be:
- HTML file
- JPEG image
- Video Stream chunk
- Audio file

Web pages consist of **base HTML-file** which includes several referenced objects.

Each object is addressable by a **uniform resource locator (URL)**, which is also sometimes referred to as a **uniform resource identifier (URI)**.

### HTTP Protocol
The HTTP application is typically associated port 80. 

![[Pasted image 20221006003504.png]]

An HTTP request message appears as such
```
GET /352/syllabus.html HTTP/1.1
Host: www.cs.rutgers.edu
User-agent: Mozilla/4.0
Connection: close
Accept-language: en
```
The first line of the message is the request line.
The lines following are the header lines. 
Following the header lines is a carriage return, which indicates the end of header.

### Method Types
- **GET** - Get the resource specified in the requested URL (could be a process)
- **POST** - Send entities (specified in the entity body) to a data-handlig process at the requested URL
- **HEAD** - Asks server to leave requested object out of response, but then send the rest of the response (useful for debugging)
- **PUT** - Update a resource at the requested URL with the new entity specified in the entity body
- **DELETE** - Deletes file specified in URL
