---
title: Problem Set 2
course: CS_352
released: YYYY-MM-DD
due: 2022-11-14
tags:
- Assignments
- CS_352
---
<center><h1>Problem Set 2</h1></center>
<center><h3>CS352 Internet Technology</h3></center>
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
1. **TCP vs. UDP (2 points)**. When is it beneficial for an application to use TCP as its transport, and when UDP?
```
   
```
2. **Computing the checksum (2 + 2 = 4 points)**. In this problem, we will get practice with computing the one’s complement of the one’s complement sum over a sequence of data values. We will use the exact same algorithm used to compute TCP/UDP checksum, but over a sequence of 4-bit chunks rather than 16-bit chunks.
   
   a.  Consider the following data bits. What is the (4-bit) checksum of this (8-bit) data? (2 points) 
   `0101 1100`
   
   b.  Consider the following data bits. What is the 4-bit checksum of this (12-bit) data (Note: you may be able to reuse calculations from part (a).) (2 points)
   `0101 1100 1001`

3. **Listing and identifying sockets. (5 points)** As we saw in a demo in class, the ss command may be used to display the listening connections and the established connections on a machine. Suppose you see the sample output shown below.
| Netid | State  | Local Addr:Port| Peer Addr:Port | Users |
| ----- | ------ | ------------ | --------- | -------------------- |
| udp   | UNCONN | 0.0.0.0:8003 | 0.0.0.0:* | (pid=29604,fd=3)     |
| tcp   | LISTEN | 0.0.0.0:8003 | 0.0.0.0:* | (pid=28832,fd=3)     |

| Netid | State | Local Addr:Port | Peer Addr:Port  | Users            |
| ----- | ----- | --------------- | --------------- | ---------------- |
| tcp   | ESTAB | 127.0.0.1:8003  | 127.0.0.1:47468 | (pid=28832,fd=4) |
| tcp   | ESTAB | 127.0.0.1:47468 | 127.0.0.1:8003  | (pid=29910,fd=3) |

The output above lists all the connections on the machine where the ss command is run. Helpfully, the last column of the output, entitled Users, also shows the process ID (pid) of the application process associated with the socket and the number of the file descriptor (fd) associated with
the socket