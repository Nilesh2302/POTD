class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        c1 = min(arr)
        c2 = max(arr)
        lcp =""
        for i in range(len(c1)):
            if c1[i]!=c2[i]:
                break
            
            lcp += c1[i]
            
        return lcp 
        