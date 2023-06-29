#User function Template for python3

class Solution:
    def createTree(self, root, l):
        # Code here
        root1 = Node(l[1])
        root2 = Node(l[2])
        root3 = Node(l[3])
        root4 = Node(l[4])
        root5 = Node(l[5])
        root6 = Node(l[6])
        
        root.left=root1
        root.right=root2
        root1.left = root3
        root1.right = root4
        root2.left = root5
        root2.right = root6
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def traverseInorder(temp, inorder):
    if(temp!=None):
        traverseInorder(temp.left, inorder)
        inorder.append(temp.data)
        traverseInorder(temp.right, inorder)
    return
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        arr= list(map(int, input().split()))
        root=Node(arr[0])
        root.left=Node(arr[1])
        root.right=Node(arr[2])
        root.left.left=Node(arr[3])
        root.left.right=Node(arr[4])
        root.right.left=Node(arr[5])
        root.right.right=Node(arr[6])
        
        
        obj=Solution()
        root0=Node(arr[0])
        obj.createTree(root0, arr)
        
        a=[]
        traverseInorder(root0, a)
        b=[]
        traverseInorder(root, b)
        
        if(a==b):
            print(1)
        else:
            print(-1)
# } Driver Code Ends