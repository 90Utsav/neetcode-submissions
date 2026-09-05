from typing import List

class Solution:

    def dfs(self, r, c, grid, visited):
        rows, cols = len(grid), len(grid[0])

        # Base cases: out of bounds, already visited, or not land (0)
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] == 0:
            return 0  # This cell does not contribute to the current island's area

        visited[r][c] = True  # Mark as visited

        current_area = 1  # This cell itself counts as 1

        # Explore neighbors and sum their contributions
        current_area += self.dfs(r + 1, c, grid, visited)
        current_area += self.dfs(r, c + 1, grid, visited)
        current_area += self.dfs(r - 1, c, grid, visited)
        current_area += self.dfs(r, c - 1, grid, visited)

        return current_area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # creating visited list:
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                # If it's land (1) and not visited, start a new DFS
                if grid[r][c] == 1 and not visited[r][c]:
                    current_island_area = self.dfs(r, c, grid, visited)
                    max_area = max(max_area, current_island_area)

        return max_area