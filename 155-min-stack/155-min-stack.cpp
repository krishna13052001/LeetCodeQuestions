class MinStack {
    stack<long long> st;
    long long min_val;
public:
    MinStack() {
        min_val = INT_MAX;
    }
    
    void push(int val) {
        long long value = val;
        if(st.empty()){
            min_val = value;
            st.push(value);
        } else {
            if(value < min_val){
                st.push(2*value - min_val);
                min_val = value;
            } else {
                st.push(value);
            }
        }
    }
    
    void pop() {
        if(st.empty()){
            return;
        }
        long long ele = st.top();
        st.pop();
        if(ele < min_val){
            min_val = 2 * min_val - ele;
        }
    }
    
    int top() {
        if(st.empty()){
            return -1;
        }
        long long ele = st.top();
        if(ele < min_val){
            return min_val;
        }
        return ele;
            
    }
    
    int getMin() {
        return min_val;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */