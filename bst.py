"""
Ms. Namasivayam
ATCS 2021-2022
Binary Tree

Python program to for binary tree insertion and traversals
"""
from bst_node import Node


'''
A function that returns a string of the inorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
def getInorder(root):
    if root.left != None and root.right != None:
        return (str(getInorder(root.left)) + '-' + str(root.val) + '-' + str(getInorder(root.right)))
    elif root.left == None and root.right == None:
        return str(root.val) 
    elif root.left == None and root.right != None:
        return (str(root.val) + '-' + str(getInorder(root.right)))
    elif root.left != None and root.right == None:
        return (str(getInorder(root.left)) + '-' + str(root.val))
       
    


'''
A function that returns a string of the postorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
# A function to do postorder tree traversal
def getPostorder(root):
    if root.left != None and root.right != None:
        return (str(getPostorder(root.left))) + '-' + str(getPostorder(root.right)) + '-' + str(root.val)
    elif root.left == None and root.right == None:
        return str(root.val)
    elif root.left == None and root.right != None:
        return (str(getPostorder(root.right))) + str(root.val) 
    elif root.left != None and root.right == None:
        return (str(getPostorder(root.left)) + '-' + str(root.val))


'''
A function that returns a string of the preorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
def getPreorder(root):
    if root.left != None and root.right != None:
        return (str(root.val) + '-' + str(getPreorder(root.left)) + '-' + str(getPreorder(root.right)))
    elif root.left == None and root.right == None:
        return str(root.val) 
    elif root.left == None and root.right != None:
        return (str(root.val) + '-' + str(getPreorder(root.right)))
    elif root.left != None and root.right == None:
        return (str(root.val) + '-'+ str(getPreorder(root.left)))


'''
A function that inserts a Node with the value
key in the proper position of the BST with the
provided root. The function will return the 
original root with no change if the key already
exists in the tree.
'''
def insert(root, key):
    current = root
    parent = None
    if root == None:
        return Node(key)
    while current != None:
        print("entered")
        parent = current
        if key < current.val:
            current = current.left
        if current == None:
            break
        if key > current.val:
            current = current.right   
    if key < parent.val:
        parent.left = Node(key)
    if key > parent.val:
        parent.right = Node(key)
    return root

'''
Challenge: A function determines if a binary tree 
is a valid binary search tree
'''
def isBST(root):
    return False


if __name__ == '__main__':
    # Tree to help you test your code
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(9)

    '''
    print("Preorder traversal of binary tree is")
    print(getPreorder(root))

    print("\nInorder traversal of binary tree is")
    print(getInorder(root))

    print("\nPostorder traversal of binary tree is")
    print(getPostorder(root))
    '''

    root = insert(root, 8)
    print("\nInorder traversal of binary tree with 8 inserted is")
    print(getInorder(root))