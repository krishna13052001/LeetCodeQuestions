class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 'N'
        x,y=0,0
        for i in range(len(instructions)):
            if(instructions[i] == 'G'):
                if(direction=='N'):
                    y += 1
                elif(direction=='S'):
                    y-=1
                elif(direction=="E"):
                    x+=1
                else:
                    x-=1
            else:
                incoming = instructions[i]
                if(direction == 'N'):
                    if(incoming=='L'):  
                        direction =  'W'
                    else:
                        direction = 'E'
                elif(direction == 'W'):
                    if(incoming=='L'):
                        direction = 'S'
                    else:
                        direction = 'N'
                elif(direction == 'S'):
                    if(incoming=='L'):
                        direction = 'E'
                    else:
                        direction = 'W'
                else:
                    if(incoming == 'L'):
                        direction = 'N'
                    else:
                        direction  = 'S'
        if((x==0 and y == 0) or direction != 'N'):
            return True
        return False
            