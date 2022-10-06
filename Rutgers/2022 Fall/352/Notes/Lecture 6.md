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
1. Cookie header line: