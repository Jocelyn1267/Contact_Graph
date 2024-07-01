# ENPM809X Project #2: Contact Graph Routing
**Due Date:** May 2, 2024, 04:00 PM

## Overview
This project involves implementing the Dijkstra algorithm on a contact graph, where nodes represent contacts between network nodes over time. The goal is to find the optimal path from a source node to a destination node by minimizing the "arrival time".

## Project Goals
Implement Dijkstra's algorithm using a minimum priority queue (heap) for efficient pathfinding in the contact graph.
Read a contact graph from the file "ContactList.txt", which contains information about contacts between network nodes over time.
Find the optimal path from node #8 to node #5 in the contact graph.
Print the contact IDs corresponding to the optimal path and the resulting best arrival time.

## Tasks
1. **Read Contact Graph Info**
   - Parse the "ContactList.txt" file to extract contact information including IDs, start time, end time, sender, receiver, and owlt attributes.

2. **Implement Minimum Priority Queue**
   - Develop a priority queue using a heap to efficiently manage and retrieve nodes based on their arrival times during Dijkstra's algorithm.

3. **Implement Dijkstra's Algorithm**
   - Adapt Dijkstra's algorithm to work with the contact graph structure.
   - Use the implemented minimum priority queue instead of a linear search for optimal performance.
   - Ignore attributes not relevant to this project such as suppr, suppr_nh, MAV, and owlt.

4. **Pathfinding**
   - Start from node #8 and compute the shortest path to node #5 based on arrival time.
   - Print the contact IDs along the optimal path and the arrival time.

## Submission Requirements
Submit the following by the project deadline:
- Complete and executable code (in C or Python) implementing Dijkstra's algorithm and priority queue.
- Well-commented code explaining the implementation details and logic.
- Output demonstrating the optimal path found from node #8 to node #5, including the contact IDs and arrival time.

## Additional Resources
Refer to sections 3 and 4 of the paper “Routing in the Space Internet: A contact graph routing tutorial” for detailed explanations of contact graph routing and Dijkstra's algorithm adaptations.
