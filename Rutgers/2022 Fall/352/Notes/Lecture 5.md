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

There are different types of DNS records.

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

### HTTP Protoc