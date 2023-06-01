class Solution:
    def reverse(self, a: int) -> int:
            
        b = str(a)
        l = []
        neg = False
        for i in b:
            if i=='-':
                neg = True
                continue
            l.append(i)
        l.reverse()
        s = ''.join(l)
        
        if int(s)<-2**31 or int(s)>2**31-1:
            return 0
        if neg:
            return int(s)*-1
        
        
        return int(s)
        