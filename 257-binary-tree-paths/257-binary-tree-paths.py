# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findAns(self,cur,res,path):
        path.append(cur.val)
        if not cur.left and not cur.right:
            res.append("->".join(map(lambda x: str(x), path)))
            return
        if cur.left:
            self.findAns(cur.left, res,path)
            path.pop()

        if cur.right:
            self.findAns(cur.right, res,path)
            path.pop()
        
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []
        self.findAns(root,res,[])
        return res