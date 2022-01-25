class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if(len(arr)<2):
            return False
        if(arr[0]<arr[1]):
            mode = "increasing"
        else:
            return False
        #mode = "increasing" if(arr[0]<arr[1])  else "decreasing"
        #print(mode)
        previous = arr[0]
        for i in range(1,len(arr)):
            if(previous<arr[i] and mode == 'increasing'):
                previous = arr[i]
            elif(previous<arr[i] and mode == "decreasing"):
                return False
            elif(previous ==arr[i]):
                return False
            elif(previous>arr[i] and mode == "increasing"):
                mode = "decreasing"
                previous = arr[i]
            elif(previous>arr[i] and mode == "decreasing"):
                #print("hi")
                previous = arr[i]
            else:
                return False
        print(mode)
        if(mode == "increasing"):
            return False
        return True