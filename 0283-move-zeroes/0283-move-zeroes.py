class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[cnt]=nums[cnt],nums[i]
                cnt+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        