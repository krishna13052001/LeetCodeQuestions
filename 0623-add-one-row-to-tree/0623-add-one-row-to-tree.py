# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node, val, depth, curr_depth):
        if node == None:
            return
        if curr_depth < depth-1:
            self.dfs(node.left, val, depth, curr_depth + 1)
            self.dfs(node.right, val, depth, curr_depth + 1)
        elif curr_depth == depth-1:
            left_node = node.left
            right_node = node.right
            new_left_node = TreeNode(val)
            new_right_node = TreeNode(val)
            node.left = new_left_node
            new_left_node.left = left_node
            node.right = new_right_node
            new_right_node.right = right_node
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode
        self.dfs(root, val, depth, 1)
        return root