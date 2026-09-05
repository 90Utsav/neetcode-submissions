from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int):
            # Stop if out of bounds or not an unvisited 'O'
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
                
            # Mark as safe/visited
            board[r][c] = 'T'
            
            # Explore all 4 neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Run DFS from all border 'O's
        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == 'O':
                    dfs(r, c)

        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == 'O':
                    dfs(r, c)

        # 2. Capture surrounded cells ('O' -> 'X') and restore safe cells ('T' -> 'O')
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
