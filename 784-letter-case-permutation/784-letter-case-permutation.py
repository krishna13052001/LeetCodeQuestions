class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        self.dfs(res,[],list(s),0)
        return res
    def dfs(self,res,lst, stringlst,index):
        if len(lst) >= len(stringlst):
            res.append("".join(lst))
            return
        if stringlst[index].isdigit():
            lst.append(stringlst[index])
            self.dfs(res,lst,stringlst,index+1)
            lst.pop()
        else:
            lst.append(stringlst[index].lower())
            self.dfs(res,lst,stringlst,index+1)
            lst.pop()
            lst.append(stringlst[index].upper())
            self.dfs(res,lst,stringlst,index+1)
            lst.pop()
            