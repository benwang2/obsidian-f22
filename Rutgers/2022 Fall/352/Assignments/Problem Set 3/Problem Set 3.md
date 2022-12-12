---
title: Problem Set 3
course: CS_352
released: YYYY-MM-DD
due: 2022-12-13
tags:
- Assignments
- CS_352
---
<center><h1>Problem Set 3</h1></center>
<center><h3>CS352</h3></center>

## Instructions

Please read and follow these instructions carefully.  
1. You must work on this problem set individually.  
2. Please complete your answers to the questions below and upload your responses to Canvas as a single PDF file.  
3. Your answers (preferably typed up rather than handwritten) must be clear, legible, and concise. If we cannot understand your answer with reasonable effort, you will get zero credit. 
4. If you leave a question out or clearly state “I don’t know”, you will receive 25% of the points for that question.  
5. We care not just about your final answer, but also how you approach the questions. In  general, if you show us your reasoning for your answers, we will do our best to provide partial credit even if your final answer is incorrect. However, if you provide no reasoning, and your answer turns out to be incorrect, you will typically receive zero points. So, please explain yourself.  
6. You are free to discuss the problem set on Piazza or through other means with your peers and the instructors. You may refer to the course materials, textbook, and resources on the Internet for a deeper understanding of topics. However, you cannot lift solutions from other students or from the web. Do not post these problems to question-answering services like Chegg. All written solutions must be your own. We run sophisticated software to detect plagiarism and carefully monitor student answers.  
7. There is a due date/time but no “time limit” on problem sets. That is, you may take as long as you need to work on problem sets, as long as you submit them on time. Further, you may make an unlimited number of submissions on Canvas. 
8. As a response to the last question of this problem set, please specify who you collaborated with, and also include all the resources you consulted to answer questions in this problem set, including URLs of pages you visited on the Internet. Also specify which question and aspect you got help with. Please be as thorough and complete as possible here. It is mandatory to answer this question.  
9. If you have any questions or clarifications on the problem set, please post them on Piazza or contact the course staff. We are here to help.
<div style="page-break-after: always;"></div>
<div style="page-break-after: always;"></div>


# Questions
There are 8 questions in this problem set totalling to 50 points.

### (1) Functional differences. (4 points)
(a) What is the key difference between the functions of the transport and network layer?

(b) What is the key difference between the control and data planes of a router?

### (2) Netmask (2 points).
Suppose hosts A and B have the same netmask M. Host A has IP address 102.45.56.7. Host B has IP address 102.46.47.8. The netmask   is 255.252.0.0. Are A and B in the same IP network? Why or why not?

### (3) Forwarding lookup (2 points).
Which field on the packet is used to lookup the router’s forwarding table? What are the consequences of using this packet field (and ignoring others)?

### (4) Benefits of IP aggregation (2 points). 
Describe any one benefit for aggregating IP addresses into IP prefixes, or aggregating smaller IP prefixes into larger ones

### (5) Fabrics (3 points)
(a) What is the benefit of using nonblocking fabrics in routers? (1.5 points)

(b) Is a crossbar fabric nonblocking? Say YES or NO. (0.5 points)

(c) Is a shared memory fabric nonblocking? Justify. (1 point)

### (6) Forwarding table matching (10 points).

Suppose a router has the forwarding table entries shown in the picture below.

| IP prefix | Output port |
| --------- | ----------- |
| 100.16.0.0/12 | 5 |
| 100.32.0.0/12 | 7 |
| 245.128.45.0/24 | 3 |
| 93.5.6.0/23 | 8 |
| 189.23.64.0/18 | 6 |
| 189.23.64.0/19 | 9 |
| 189.23.96.0/19 | 10 |

For the questions below, partial credit will be provided if you explain the reasoning behind your answers.

(a) Suppose a packet enters the router with a source IP address of 93.5.6.145 and a destination IP address of 245.128.45.168. What output port is it forwarded to? (2 points)

(b) Suppose another packet arrives with a destination IP address of 100.31.105.54. What output port is it forwarded to? (3 points)

(c) Suppose another packet arrives with a destination IP address of 189.23.80.4. What output port is it forwarded to? (3 points)

(d) Suppose another packet arrives with a destination IP address of 8.8.8.8. What output port is it forwarded to? (2 points)

### (7) Intra-domain routing protocols (27 points)
Consider the network whose graph abstraction is shown in this picture. The IP prefixes “owned” by the router, i.e., the set of endpoints reachable directly through the router, are provided alongside the routers, labeled and identified as A, B, C, etc. The link metrics are shown next to the edges in the graph.

![[Pasted image 20221212155353.png]]

(a) Suppose the network uses a link state routing protocol. Populate the following information in the link state advertisement originating from router B. (5 points)

router ID: $B$

IP prefix owned by the router (1 point): ``
IDs of neighboring routers (2 points):
Link metrics to neighbors (2 points):
(For the last question, please write the metrics in the same order as the neighbor IDs before.)