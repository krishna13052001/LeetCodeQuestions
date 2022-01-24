class Solution:
    digit2letters = { '2' : 'abc', '3':'def','4':'ghi','5':'jkl','6':'mno', '7':'pqrs','8':'tuv','9':'wxyz' }
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        self.dfs_traverse(digits,"",result)
        return result
    def dfs_traverse(self,string,cur,res):
        if(not string):
            if (cur):
                res.append(cur)
            return
        for let in self.digit2letters[string[0]]:
            self.dfs_traverse(string[1:],cur+let,res)
            
            
        