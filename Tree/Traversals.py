"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    #Write your code here
    if root == None:
        return
    print(root.data, end= " ")
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    #Write your code here
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end= " ")

def inOrder(root):
    #Write your code here
    if root == None:
        return
    inOrder(root.left)
    print(root.data,end= " ")
    inOrder(root.right)