# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,ans):
        if(root!=None):
            self.inorder(root.left,ans)
            ans.append(root.val)
            self.inorder(root.right,ans)
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = []
        l2 = []
        res = []
        self.inorder(root1,l1)
        self.inorder(root2,l2)
        length1 = len(l1)
        length2 = len(l2)
        i = j = k =0
        while(i<length1 and j<length2):
            if(l1[i]<=l2[j]):
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        while(i<length1):
            res.append(l1[i])
            i +=1
        while(j<length2):
            res.append(l2[j])
            j += 1
        return res