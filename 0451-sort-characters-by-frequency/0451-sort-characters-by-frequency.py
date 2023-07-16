class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            
            else:
                d[i] = 1
        
        d1 = dict(sorted(d.items(),key=lambda item : item[1],reverse=True))
        
        ans = ""
        for i in d1:
            ans += i * d[i]
            
            
        
        return ans
        