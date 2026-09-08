class Solution:


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list=[[] for i in range(n)] 
        res1= []
        visited=[False for i in range(n)]
        for a,b in edges: #making adjency list
            adj_list[b].append(a)
            adj_list[a].append(b)

        def dfs(adj_list, visited, s, res): 
            visited[s] = True 
            res.append(s)


            for i in adj_list[s]: 
                if not visited[i]: 
                    dfs(adj_list, visited, i, res)    
        for i in range(n): 
            if not visited[i]: 
                component=[]
                dfs(adj_list, visited, i, component)
                res1.append(component)
        return len(res1)
