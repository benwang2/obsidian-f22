---
title: Lecture Notes 6
course: CS_XXX
date: YYYY/MM/DD
tags: 
- lectureNotes
- CS_XXX
---

<center><h1>Lecture 6</h1></center>

## HTTP Cookies

HTTP mechanisms are **stateless** - each request is processed independently and the server maintains no memory about past client requests.

#stateless, #states, #cookies

**State** is essential in servicing users. Using states, we are able to implement features such as user authentication, shopping carts, video recommendations, and any user session state in general.

### How it works
Cookies keep a users memory. The **client and server collaborate** to track user state.

There are four components of a cookie:
1. Cookie header line of **HTTP response message**
2. Cookie header line in **HTTP response message**
3. Cookie file kept on userd endpoint, managed by user's browser
4. Back-end database maps cookie to user data at Web endpoint

### Cookie usage
Cookies can be used in many different ways, some good, some bad, and some ugly. For an internet user, the most common ways a they will experience cookies in use is in shopping carts, user authentication, etc.

Some uses of cookies are bad. They unnecessarily record activities across the site for performance statistics, user engagement, and more.

Cookies can be used to intrude on a user's privacy. Third party cookies that are played by ads and tracking networks can track activities across the internet. This usage of cookies leads to potentially personally identifiable information being contained in cookies.

## Web caching
Web caches are machines that remember web responses for a network.

They reduce the response time for client requests and reduce traffic on an institution's access link.

Devices can be configured to use an HTTP proxy. If a proxy for a device is set, all HTTP requests will be sent to the proxy (cache).

On a cache hit, the cache returns the object.
On a cache miss, the cache obtains the object from the originating web server (**origin server**) and returns the object to client. It also caches it locally.

```mermaid
flowchart
client1("Laptop") -->|1| proxy("Proxy server")
proxy -->|2| origin("Origin server")
origin -->|3| proxy
proxy -->|4| client1
client2("Tablet") -->|5| proxy
proxy >
```