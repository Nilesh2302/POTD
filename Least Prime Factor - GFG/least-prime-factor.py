#User function Template for python3
class Solution:
    def cP(self,i):
        for j in range(2,i):
            if i%j==0:
                return False
        
        return True        
    def leastPrimeFactor (self, N):
        # arr = []
        # for i in range(n+1):
        #     if i==0:
        #         arr.append(0)
        #         continue
            
        #     if i==1:
        #         arr.append(1)
        #         continue
            
        #     if i==2:
        #         arr.append(2)
        #         continue
            
        #     if i==3:
        #         arr.append(3)
        #         continue
            
            
            
        #     for j in range(2,i+1):
        #         if self.cP(j)==True:
        #             if i%j==0:
        #                 arr.append(j)
        
        # return arr          
        ans = [1] *(N+1)
        for i in range(2,N+1):
            if ans[i] == 1:
                ans[i] = i
            for j in range(i,N+1,i):
                if ans[j] == 1:
                    ans[j] = i
        return ans
                        
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.leastPrimeFactor(n)
		for i in range(1, n+1):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends