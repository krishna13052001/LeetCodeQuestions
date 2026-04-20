# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root):
            if root:
                tmp = root.left
                root.left = root.right
                root.right = tmp
                inorder(root.left)
                inorder(root.right)
                return root
        return inorder(root)