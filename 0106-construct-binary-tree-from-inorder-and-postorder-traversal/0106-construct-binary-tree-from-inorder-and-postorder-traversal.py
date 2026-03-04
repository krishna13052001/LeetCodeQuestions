# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inmap = {}
        for idx in range(len(inorder)):
            inmap[inorder[idx]] = idx
        return self.build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1, inmap) 
    def build(self, inorder, instart, inend, postorder, poststart, postend, inmap):
        if instart > inend or poststart > postend:
            return None
        
        root = TreeNode(postorder[postend])
        innode = inmap[postorder[postend]]
        numsLeft = innode - instart

        root.left = self.build(inorder, instart, innode -1, postorder, poststart, poststart + numsLeft - 1, inmap)
        root.right = self.build(inorder, innode +1, inend, postorder, poststart + numsLeft, postend -1, inmap)
        return root
