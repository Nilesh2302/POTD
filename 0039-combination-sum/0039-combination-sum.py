class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        
        def findcombination(ind,target):
            if ind == len(candidates):
                if target == 0:
                    ans.append(ds[:])
                return
            
            if candidates[ind] <= target:
                ds.append(candidates[ind])
                findcombination(ind,target-candidates[ind])
                ds.pop()   # this for removal adding element when we backtrack
                
            findcombination(ind+1, target)
        findcombination(0,target)
        return ans
        