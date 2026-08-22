"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #  we can't return same graph
        #In mathematics and computer science, connectivity is one of the basic concepts of graph theory: It is closely related to the theory of network flow problems. The connectivity of a graph is an important measure of its resilience as a network.


        #The resulting object is called an object copy or simply copy of the original object. Copying is basic but has subtleties and can have significant overhead. There are several ways to copy an object, most commonly by a copy constructor or cloning.

        """
        
                    GRAPH
                    │
            ┌───────┴────────┐
            ↓                ↓
        What is asked?    What type?
            │                │
            ↓                ↓
        Reachability        Directed?
        Shortest path       Undirected?
        Cycle?              Weighted?
        Components?         Unweighted?
        Ordering?
            │
            ↓
        Choose algorithm
            │
            ├── DFS
            ├── BFS
            ├── Dijkstra
            ├── Union-Find
            └── Topological Sort
        
        """
        # Edge case: if the graph is empty
        if not node:
            return None
            
        # Step 1: Initialize our dictionary to track visited nodes
        # Key: Original Node | Value: Cloned Node
        visited = {}
        def dfs(current_node):
            if current_node in visited:
                return visited[current_node]
            ## Step 3: Create the clone and store it IMMEDIATELY
            clone=Node(current_node.val)
            visited[current_node]=clone
            # Step 4: Build the connections by iterating through neighbors
            for neighbor in current_node.neighbors:
                # Recursively call dfs on the neighbor and append the result
                clone.neighbors.append(dfs(neighbor))
                
            return clone
            
        # Start the traversal from the given reference node
        return dfs(node)