# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        idx = 0

        def bstFromPreorder(preorder, bound):
            nonlocal idx
            if idx == len(preorder) or preorder[idx] > bound:
                return None
            root = TreeNode(preorder[idx])
            idx += 1
            root.left = bstFromPreorder(preorder, root.val)
            root.right = bstFromPreorder(preorder, bound)
            return root
        return bstFromPreorder(preorder,float("inf"))