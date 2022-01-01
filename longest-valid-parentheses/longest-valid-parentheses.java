class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        int ans = 0;
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            // System.out.println("hahaha"+c);
            if(c=='('){
                stack.push(i);
                System.out.println(i);
            } else {
                stack.pop();
                if(stack.isEmpty()){
                    stack.push(i);
                } else {
                    int len = i - stack.peek();
                    ans = Math.max(ans,len);
                }
            }
        }
        // System.out.println("hey hey");
        // if(!stack.isEmpty()){
        //     int len = s.length() - stack.peek();
        //     ans = Math.max(len,ans);
        // }
        return ans;
    }
}