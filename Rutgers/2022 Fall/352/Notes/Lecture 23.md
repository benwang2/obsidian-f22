---
title: Lecture Notes 23
course: CS_352
date: 2022-12-06
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 23</h1></center>

## Control plane
The control plane is **distributed** throughout routers. Components in every router interact with other components to produce a routing outcome. 

Data plane performs per-packet processing, moving packet from input port to output port.

Routing algorithms work over an abstract representation of the network, called **the graph abstraction**.

Each router is a **node** in a graph and each link is an **edge** in the graph. Additionally, edges have **weights** (called **link metrics**) which is set by netadmin.

The cost of an edge is defined as **c(x, y)** and the cost of a path is the **sum of the edge costs.**

Each node should determine the least cost path to every other node.

## Routing protocols
>Routing protocols include link state protocols and distance vector protocols.

### Link State Protocols
With link state protocol, each router knows the **state** of all the links and routers in the network. Every router performs an **independent** computation on **globally shared** knowledge of network's **complete** graph representation.

#### Information exchange

**Link state flooding** is the process by which neighborhood information of **each network router** is transmitted to **all other routers**.

Each router sends a **link state advertisement** (LSA) to each of its neighbos, containing:
- router ID
- IP prefix owned by router
- router's neighbors
- link cost to those neighbors

Upon receiving an LSA, a router forwards it to each of its neighbors: **flooding**

Eventually, the entire network receives LSAs from each router, which are put into a **link state database**.

LSAs still occur periodically **whenever the graph changes**, like if a link fails or a new link or router is added.

The routing algorithm running at each router can **use the entire network's graph** to compute least cost paths.

#### Dijkstra's Algorithm
The link state protocol uses **Dijkstra's** algorithm.
- Given a network graph, the algorithm computes the least cost paths from one node (source) to all other nodes
- This can be used to compute the forwarding table at that node
- The algorithm maintains **estimates** of least costs to reach every other node. After $k$ iterations, each node definitively knows teh least cost path to $k$ destinations.

Notation used in the algorithm is written as following:
- $c(x,y)$: the link cost from node $x$ to $y$; it is $\infty$ if not direct neighbors
- $D(v)$: current estimate of path from source to destination $v$
- $p(v)$: (predecessor node) the last node before $v$ on the path from source to $v$
- $N'$: set of nodes whose least cost path is definitively known

##### Explanation
```
N' = {u}
for v' in v:
	if v' adjacent to u:
		D(v) = c(u,v)
	else:
		D(v) = ∞

repeat
	find w not in N' such that D(w) is a minimum
		add w to N'
		update D(v) for all v adjacent to w and not in N':
			D(v) = min( D(v), D(w) + c(w,v) )
until all nodes in N'
```

**Relaxation**: for each $v$ in $V/N'$, is the cost of the path via $w$ smaller than knownleast cost path to $v$? If so, update $D(v)$. Predecessor of $v$ is $w$.

