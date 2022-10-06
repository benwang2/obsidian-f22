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
- **value** is name of

