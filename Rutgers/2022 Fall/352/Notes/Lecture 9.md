---
title: Lecture Notes 9
course: CS_352
date: 2022/10/04
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 9</h1></center>

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

#DASH

#### Key ideas
The video, audio, and transcript content are divided into segments (**time**).

There must be algorithms to determine and request varying attributes for each segment (bitrate, language, resolution).

The goal of dash is to ensure good quality of service and to match user preferences.

### Example
The browser has a media player and is an HTTP client, so it can make and receive HTTP requests.

Before streaming, the server must inform the client of the **media presentation description (manifest)**.

Using the manifest, the HTTP client makes requests based on time, and then picks attributes for each segment of content.

### Manifest
Fundamentally, the manifest contains:
- periods (Media Presentation Duration: **MPD**)
- adaptation set
- representations
- functional equivalent: representation set of adaptation set

[dash example](https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html)

The forward-most portion of the manifest contains the periods (durations of contents). 

From a period, we may access a list of adaptation sets, which is functionally equivalent content. It contains various adaptation sets. Eah adaptation set indicates what the media type is, and other attributes about the set.

From an adaptation set, we can access a representation. The representation tells you about the attributes:
- codecs
- bandwidth
- width
- height
- frame rate
- scan type

In each representation, attributes for multiple segments are included. The segment itself is not downloaded, but a resource URL is provided for each media segment.

Byte ranges per segment are provided (HTTP header for a **range segment**)

%%What's a range segment?%%

## Transport layer
The transport layer contains the UDP and TCP protocol. It is a communication abstractoin between proccesses and delivers packets to the process.

### Transport services and protocols
The services and protocols provide a communication abstraction between application processes.

Transport protocols run endpoints. On the *send side*, app messages are broken into **segments** and then passed to the network layer. On the *recv side*, segments are reassembled into messages, and then passed to the app layer.

TCP and UDP are very popular transport protocols.

## Network layer
The network layer is an abstraction to communicate between **endpoints**. The network layer provides best effort packet delivery to a remote endpoint.

## Questions
