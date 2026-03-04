# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for idx in range(len(inorder)):
            inorder_map[inorder[idx]] = idx
        
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder)-1, inorder_map)
    
    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inordered_map):
        if preStart > preEnd or inStart > inEnd:
            return None
        root = TreeNode(preorder[preStart])
        inRoot = inordered_map[root.val]
        numsLeft = inRoot - inStart
        root.left = self.build(preorder, preStart + 1, preStart + numsLeft, inorder, inStart, inRoot - 1, inordered_map)
        root.right = self.build(preorder, preStart + numsLeft + 1, preEnd, inorder, inRoot + 1, inEnd, inordered_map)
        return root