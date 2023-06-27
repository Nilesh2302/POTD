class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        maxcnt=0
        for i in nums:
            if i==1:
                cnt+=1
                if cnt>maxcnt:
                    maxcnt=cnt
            
            else:
                cnt=0
                
        return maxcnt