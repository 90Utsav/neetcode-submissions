class Solution:
    def dfs(self,i,j,grid,visited): 
        

        # Base case: if out of bounds, water, or already visited, return
        if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0' or visited[i][j]):
            return
        visited[i][j]=True
        self.dfs(i+1,j,grid,visited)
        self.dfs(i-1,j,grid,visited)
        self.dfs(i,j+1,grid,visited)
        self.dfs(i,j-1,grid,visited)

        



    def numIslands(self, grid: List[List[str]]) -> int:
        row, cols=len(grid), len(grid[0])
        visited=[[False for _ in range(cols)] for _ in range(row)]
        ans=0 

        for i in range((row)): 
            for j in range(cols): 
                if grid[i][j]=="1" and not visited[i][j]: 
                    self.dfs(i,j,grid,visited)
                    ans+=1
            
        return ans