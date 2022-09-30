---
title: Lecture Notes 8
course: CS 352
date: 2022/09/30
tags: "Lecture Notes"
---

# Lecture 8
## Internet Multimedia Applications
Many applications on the internet use audio or video. By 2022, 82% of all IP traffic will be IP video traffic, up from 75% in 2017.

e.g. Netflix, Spotify, Zoom, YouTube

These applications run over HTTP / HTTPS, and SMTP. They are delay tolerant, but not loss tolerant.

These kinds of applications often work in **real time** and therefore data delivery time during transfer matters for UX. Data delivery must be continuous for a smooth UX. Data is used only **after** transfer is complete.

Real-time audio and video can be somewhat loss tolerant, but a delay of over 400 ms will result in a bad UX. (e.g. Zoom, Skype, Discord)

[[smtp]]
[[http]]