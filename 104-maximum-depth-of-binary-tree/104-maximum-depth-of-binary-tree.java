/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int helper(TreeNode root,int count){
        if(root == null){
            return count;
        }
        int left_depth = helper(root.left,count+1);
        int right_depth = helper(root.right,count+1);
        return Math.max(left_depth,right_depth);
    }
    public int maxDepth(TreeNode root) {
        return helper(root,0);
    }
}