# In this Question we have to use Binary tree and queue for storing node.
# It will O(n) space and O(n) time
# We can do it using BSt also

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if not root:
        root = Node(key)
        return root
    q = []
    q.append(root)
    while (len(q)):
        temp = q[0]
        q.pop(0)
 
        if (not temp.left):
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
 
        if (not temp.right):
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)
    return root
def countNodes(root, key):
    if not root:
        return 0
        
    count = 0
    if root.val < key:
        count += 1
    
    count += countNodes(root.left, key)
    count += countNodes(root.right, key)
    
    return count
    
    
root = Node(6)    
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 51)
root = insert(root, 59)
root = insert(root, 25)
print(countNodes(root, 51))