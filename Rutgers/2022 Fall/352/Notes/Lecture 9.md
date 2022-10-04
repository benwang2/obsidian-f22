---
title: Lecture Notes 9
course: CS_352
date: 2022/10/04
tags: 
- lectureNotes
- CS_352
---

# Lecture 9

## On-demand Video Streaming
The processof streaming a stored video has a couple of challenges:
- continuous playout constraint
- variable network delays
- client interactivity

### Client-side buffering
Clients have a **client-side buffer** of downloaded video to absorb variatoin in network conditions.

Review lecture materials and take notes...
[lecture notes](https://people.cs.rutgers.edu/~sn624/352-S22/lectures/08-video-streaming.pdf)


## Dynamic Adaptive Streaming over HTTP (DASH)

The DASH standard is used by almost all notable video streaming service.

The streaming is *dynamic* because the video can be retrieved from multiple sources.

The streaming is *adaptive*, the bit rate can be adapted on the client or the server (using client feedback).

The DASH video server is just a standard HTTP server that provides video/audio content in multiple formats and encodings. As a result, we can leverage existing web-based infrastructures like DNS and CDNs.

DASH allows for very large videos to be rendered by clients, taking advantage of CDNs.

