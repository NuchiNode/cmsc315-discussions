# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

The Breadth-First Search algorithm was difficult to grasp at first, but with trial and error, I started to understand 
how BFS moves through a graph and how a graph works logically. I used a small computer network where the nodes 
represented routers, switches, and servers, and the edges represented the connections between them. Using a network 
example made it easier for me to understand how BFS moves through connected nodes one level at a time.

One challenge I had was understanding how the queue and visited set worked together. The queue keeps track of which node
should be checked next, while the visited set prevents the same node from being added more than once. I also ran into an
error when I misspelled Server4 and connected it to the wrong node. Fixing the graph entry helped me understand how 
important the adjacency list is to the traversal.

BFS uses a queue and checks nearby nodes first, while DFS normally follows one path as far as possible before going 
back. BFS would be useful for finding nearby connections or shortest paths in an unweighted graph. DFS can be useful 
when exploring deeper paths or searching through an entire structure.
