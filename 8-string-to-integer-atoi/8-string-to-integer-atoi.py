class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if(s == ""):
            return 0
        flag = 1
        i = 0
        if(s[0]=="-"):
            flag = 0
            i = 1
        elif(s[0] == "+"):
            i = 1
        length = len(s)
        # print(s)
        while(i< length and s[i] == '0'):
            i += 1
        start = i
        while(i<length):
            try:
                k = int(s[i])
                # print(k,start,i)
            except:
                break
            i += 1
        if(start == i):
            return 0
        interger = int(s[start:i])
        if(flag == 0):
            interger *= -1
            if(interger< -2147483648):
                return -2147483648
            return interger
        if(interger > 2147483647):
            return 2147483647
        return interger
                
        