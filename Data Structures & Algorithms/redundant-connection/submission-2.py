class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import deque
        #making adj_list: 
        n = len(edges)+1 # number of nodes: 
        adj_list = [[]for i in range(n)]

        indegree=[0]*n

        for a,b in edges: 
            adj_list[a].append(b)
            adj_list[b].append(a)
            indegree[a]+=1
            indegree[b]+=1
        
        q = deque()

        for i in range(n): 
            if indegree[i] == 1: 
                q.append(i)
        
        while q: 
    
            front = q.popleft()
            indegree[front] -=1

            for nei in adj_list[front]: 
                indegree[nei]-=1 

                if indegree[nei] == 1: 
                    q.append(nei)
        for u, v in reversed(edges): 
            if indegree[u] == 2 and indegree[v] ==2 : 
                return [u,v]
        return []

