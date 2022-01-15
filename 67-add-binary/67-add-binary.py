class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        return bin(a+b)[2:]
    
    '''def addBinary(self,a:str,b:str)->str:
        if(len(a)>len(b)):
            # swap the number 
            a,b = b,a
        a,b = list(a),list(b)
        # we should add from left signifacte bit
        a.reverse()
        b.reverse()
        for i in range(len(a)):
            if a[i] == '0':
                continue
            elif(b[i] == 0):
                b[i] = "1"
                continue
            else:
                b[i] = '0'
                # when two strings of same length
                if (i == len(b)-1):
                    b.append("1")
                else:
                    for j in range(i+1,len(b)):
                        if(b[j] == '0'):
                            b[j] = '1'
                            break
                        else:
                            b[j] = '0'
                            if(j==len(b)-1):
                                b.append("1")
                                break
        b.reverse()
        return ''.join(b)'''
                