# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def find_ans(headp, headq) -> bool:
            if headp == None and headq == None:
                return True
            elif headp == None and headq != None:
                return False
            elif headp != None and headq == None:
                return False
            left = find_ans(headp.left, headq.left)
            right = find_ans(headp.right, headq.right)
            if not left or not right:
                return False
            if headp.val == headq.val:
                return True
            else:
                return False
        return find_ans(p, q)