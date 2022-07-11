/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int helper(TreeNode* root, int count){
        if(root == NULL){
            return count;
        }
        int left_depth = helper(root->left,count+1);
        int right_depth = helper(root->right,count+1);
        return max(left_depth,right_depth);
    }
    int maxDepth(TreeNode* root) {
        return helper(root,0);
    }
};