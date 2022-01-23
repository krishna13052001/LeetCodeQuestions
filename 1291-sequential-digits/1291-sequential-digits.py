class Solution:
    # self.ans = []
    def dfs(self,low,high,i,num,ans):
        if(num >= low and num <= high):
            ans.append(num)
        if(num>high or i>9):
            return
        self.dfs(low,high,i+1,num*10+i,ans)
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1,10):
            self.dfs(low,high,i,0,ans)
        ans.sort()
        return ans