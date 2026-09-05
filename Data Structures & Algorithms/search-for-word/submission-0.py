class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS=len(board), len(board[0])
        path=set()

        #making a function for dfs kind of thing, so basically we are exploring everypossible neighboour of the current cell we are on and then just brute forcing into finding wether that work exists of not:

        def dfs(r,c,i): 
            if i==len(word): 
                return True 
            
            if (min(r, c) < 0 or
                    r >= ROWS or c >= COLS or
                    word[i] != board[r][c] or
                    (r, c) in path):
                    return False
            path.add((r,c))

            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res


        for r in range(ROWS): 
            for c in range(COLS): 
                if dfs(r,c,0): 
                    return True
        return False
            