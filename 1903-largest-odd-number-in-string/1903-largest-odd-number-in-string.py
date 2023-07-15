class Solution:
    def largestOddNumber(self, num: str) -> str:
        temp = num
        temp = temp[::-1]
        cnt=0
        for i in temp:
            if int(i)%2==1:
                break
            cnt+=1    
        
        temp = temp[cnt:]
        temp = temp[::-1]
        return temp
        