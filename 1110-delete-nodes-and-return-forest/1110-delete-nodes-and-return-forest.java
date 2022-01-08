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
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        HashSet<Integer> set = new HashSet<>();
        for(int i:to_delete){
            set.add(i);
        }
        ArrayList<TreeNode> ans = new ArrayList<>();
        this.findResult(root,set,ans);
        if(!set.contains(root.val)){
            ans.add(root);
        }
        return ans;
    }
    public TreeNode findResult(TreeNode root, HashSet<Integer> set, ArrayList<TreeNode> ans){
        if(root.left != null){
            root.left = findResult(root.left,set,ans);    
        }
        if(root.right != null){
            root.right = findResult(root.right,set,ans);   
        }
        if(set.contains(root.val)){
            if(root.left!=null){
                ans.add(root.left);
            }
            if(root.right != null){
                ans.add(root.right);
            }
            return null;
        }
        return root;
    }
}