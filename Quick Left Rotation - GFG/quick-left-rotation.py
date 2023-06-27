class Solution:
    def leftRotate(self, arr, k, n):
        k = k%n
        i=0
        j=k-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        
        
        i=k
        j=n-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        
        arr.reverse()        
            
            
        


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends