---
title: Lecture Notes 8
course: CS_352
date: 2022/09/30
tags: 
- Lecture Notes
- CS_352
---

# Lecture 8
## Internet Multimedia Applications
Many applications on the internet use audio or video. By 2022, 82% of all IP traffic will be IP video traffic, up from 75% in 2017.

e.g. Netflix, Spotify, Zoom, YouTube

These applications run over HTTP / HTTPS, and SMTP. They are delay tolerant, but not loss tolerant.

These kinds of applications often work in **real time** and therefore data delivery time during transfer matters for UX. Data delivery must be continuous for a smooth UX. Data is used only **after** transfer is complete.

Real-time audio and video can be somewhat loss tolerant, but a delay of over 400 ms will result in a bad UX. (e.g. Zoom, Skype, Discord)

#smtp
#http
#multimedia

### Digital Representation of Audio
Audio must be converted from an analog signal to a digital representation. Originally, it is a continuous time system, and the system takes samples at different time points in the audio.

#### Sampling
The standard is to sample the song $n=2*max(f)$, where $f$ is the frequencies in the signal.

#sampling

#### Quantize
Following the sampling process, the samples are quantized to levels and bits. *what is quantizing?* This creates a more accurate representation of the signal. A higher accuracy representation results in larger data.

#quantize

#### Compression
With #compression, create a compact representation of quantized values.

#### Examples
**Telephone:** 8,000 samples/sec or bytes/sec

$Bandwidth=8,000*8=64,000bps$
The receiver converts the bits back to an analog signal and the quaity is reduced in the process.

**CD music:** 44,100 samples/sec or 1.411 Mb/s
**MP3:** 96, 128, 160 Kbps
**Internet telephony:** 5.3 Kbps and up

### Video Representation
A digital image is represented as an array of pixels. Each pixel is represented by bits, with the number of pixels being the resolution. A higher amount of pixels results in higher quality, and a lower amount results in a lower quality. In each pixel, the luminance and color is encoded.

Use redundancy within and between images to decrease numbe rof bits used to encode image.

#### Spatial coding (within image)
Instead of sending N values of same color, send only two values:
- color value ( purple )
- number of repeated values ( N )

#spatial_coding

#### Temporal coding (from one image to next)
Instead of sending complete frame at $frame_{i+1}$, send only differences from frame $frame_i$ (motion vectors).

#temporal_coding

The coding/decoding algorithm used is often called a #codec.

#### Terminology

**Video bit rate** is the effective number of bits per second of the video after encoding.

The bit rate depends on many factors:
- resolution of each image: more pixels = more bits
- detail per pixel: better luminance and color detail = more bits
- amount of movement in video:  = more bits
- quality of overall compression in code

The video bit rate is commonly correlated with the quality of perception.

The bit-rate of a video changes over the duration of the video.

**CBR** (constant bit rate): fixed bit-rate video
**VBR** (variable bit rate): different parts of the video have different bit rates. (e.g. changes in color, motion, etc.)

For VBR, there is an **average bit-rate** that can be computed over the video's duration. Some examples of this are...
- MPEG 1 (CD-ROM) - 1.5 Mbps
- MPEG 2 (DVD), 3-6 Mbps
- MPEG 4 ,< 1 Mbps

### Networking multimedia
- On-demand streamed video/audio
- ...
- ...

### On demand
