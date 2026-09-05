class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[] 

        res=[]
        def main_function(open,close): 
            if open==close==n: 
                res.append("".join(stack))
                return
            
            if open<n: 
                stack.append("(")
                main_function(open+1, close)
                stack.pop()


            if open>close: 
                stack.append(")")
                main_function(open, close+1)
                stack.pop()
        
        main_function(0,0)
        return res