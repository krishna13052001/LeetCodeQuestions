# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        head = root
        while True:
            if head.val < val:
                if head.right:
                    head = head.right
                else:
                    head.right = TreeNode(val)
                    break
            elif head.val > val:
                if head.left:
                    head = head.left
                else:
                    head.left = TreeNode(val)
                    break
        return root

