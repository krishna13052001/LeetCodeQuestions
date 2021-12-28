# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findAns(self,root,count):
        if not root:
            return count
        if root.left == None:
            return self.findAns(root.right,count+1)
        if root.right == None:
            return self.findAns(root.left,count+1)
        
        left_depth = self.findAns(root.left,count+1)
        right_depth = self.findAns(root.right,count+1)
        # print(count,"..........")
        # if(left_depth == count or right_depth == count):
        #    return max(left_depth,right_depth)
        return min(left_depth,right_depth)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.findAns(root,0)