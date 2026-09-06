class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        from collections import deque 

        q=deque()
        n=numCourses
        adj_list=[]
        indegree=[0]*n 
        ans=[] 

        #making adj_list: 
        for i in range(n): 
             adj_list.append([])


        for target, prereq in prerequisites:
            adj_list[prereq].append(target)
        #inordering: 
        for a,b in prerequisites: 
            indegree[a]+=1
        
        for i in range(n): 
            if indegree[i] == 0: 
                q.appendleft(i)
                ans.append(i)

        while len(q) > 0: 
            front = q.popleft()

            for i in adj_list[front]: 
                indegree[i]-=1
                if indegree[i]==0: 
                    q.appendleft(i)
                    ans.append(i)
            
        return len(ans)==n


            