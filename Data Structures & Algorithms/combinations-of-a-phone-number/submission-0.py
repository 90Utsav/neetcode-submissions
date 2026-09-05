class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict={ 
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        output=[]

        def backtrack(i,curr_pair): 
            if len(digits)==len(curr_pair): 
                output.append(curr_pair)
                return 
            
            
            for x in dict[digits[i]]: 
                backtrack(i+1, curr_pair+x)

        if digits: 
            backtrack(0,"")
        return output

        
