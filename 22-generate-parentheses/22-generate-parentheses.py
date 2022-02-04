class Solution:
    def findAns(self,n,res,ans,open,close):
        # print(open,close)
        if(open == 0 and close == 0):
            # print(ans)
            res.append("".join(ans))
            return
        if(open != 0):
            ans.append('(')
            self.findAns(n,res,ans,open-1,close)
            ans.pop()
        if(open<close):
            ans.append(")")
            self.findAns(n,res,ans,open,close-1)
            ans.pop()
            return
            
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        count = [0]
        ans = []
        self.findAns(n,res,ans,n,n)
        return res