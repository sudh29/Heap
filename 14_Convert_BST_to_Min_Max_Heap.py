#User function Template for python3
import heapq
'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''
def inorder_traversal(root, arr):
    if root:
        inorder_traversal(root.left, arr)
        arr.append(root.data)
        inorder_traversal(root.right, arr)
        
def preorder_traversal(root, arr, idx):
    if root:
        idx[0]+=1
        root.data = arr[idx[0]]
        postorder_traversal(root.left, arr, idx)
        postorder_traversal(root.right, arr, idx)
        
def postorder_traversal(root, arr, idx):
    if root:
        postorder_traversal(root.left, arr, idx)
        postorder_traversal(root.right, arr, idx)
        root.data = arr[idx[0]]
        idx[0]+=1

class Solution:
    def convertToMaxHeapUtil(self, root):
        if not root:
            return
        arr = []
        inorder_traversal(root, arr)
        postorder_traversal(root, arr, [0])
        
    def convertToMinHeapUtil(self, root):
        if not root:
            return
        arr = []
        inorder_traversal(root, arr)
        preorder_traversal(root, arr, [0])
        
#{ 
 # Driver Code Starts
# Initial Template for Python

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
def postOrder(root):
    if root==None:
        return 
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=" ")
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob= Solution()
        
        ob.convertToMaxHeapUtil(root)
        postOrder(root)
            
        print()
        
        

# } Driver Code Ends
