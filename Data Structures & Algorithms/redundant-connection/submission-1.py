from collections import deque
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        # Nodes are 1-indexed from 1 to n
        adj_list = [[] for _ in range(n + 1)]
        degree = [0] * (n + 1)
        
        # 1. Build the adjacency list and record initial degrees
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        # 2. Add all current leaves to the queue
        q = deque()
        for i in range(1, n + 1):
            if degree[i] == 1:
                q.append(i)
                
        # 3. Peel the leaves layer by layer
        while q:
            curr = q.popleft()
            
            # Decrement the neighbor's degree as this leaf is logically removed
            for nei in adj_list[curr]:
                degree[nei] -= 1
                
                # If a neighbor becomes a leaf, queue it up
                if degree[nei] == 1:
                    q.append(nei)
                    
        # 4. Find the redundant edge
        # Any node that remains with a degree of 2 is part of the cycle.
        # We iterate backward to find the LAST edge in the input connecting two cycle nodes.
        for u, v in reversed(edges):
            if degree[u] == 2 and degree[v] == 2:
                return [u, v]
                
        return []