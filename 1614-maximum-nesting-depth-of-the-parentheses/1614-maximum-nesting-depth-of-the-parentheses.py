class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        op = 0
        for i in s:
            if i =='(':
                op+=1
            
            elif i == ')':
                op -=1
            
            depth = max(depth,op)
        
        return depth
        