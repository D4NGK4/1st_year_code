# A utility function to search a given key in BST
def search(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
   
    # Key is smaller than root's key
    return search(root.left,key)
 
# This code is contributed by Bhavya Jain

# Python program to demonstrate
# insert operation in binary search tree
 
# A utility class that represents
# an individual node in a BST
 
 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# A utility function to insert
# a new node with the given key
 
 
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
 
# A utility function to do inorder tree traversal
 
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 
 
# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
 
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
 
# Print inoder traversal of the BST
inorder(r)

# Python program to demonstrate delete operation
# in binary search tree

# A Binary Tree Node


class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# A utility function to do inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print (root.key,end=" ")
		inorder(root.right)


# A utility function to insert a
# new node with given key in BST
def insert(node, key):

	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node

# Given a non-empty binary
# search tree, return the node
# with minimum key value
# found in that tree. Note that the
# entire tree does not need to be searched


def minValueNode(node):
	current = node

	# loop down to find the leftmost leaf
	while(current.left is not None):
		current = current.left

	return current

# Given a binary search tree and a key, this function
# delete the key and returns the new root


def deleteNode(root, key):

	# Base Case
	if root is None:
		return root

	# If the key to be deleted
	# is smaller than the root's
	# key then it lies in left subtree
	if key < root.key:
		root.left = deleteNode(root.left, key)

	# If the kye to be delete
	# is greater than the root's key
	# then it lies in right subtree
	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	# If key is same as root's key, then this is the node
	# to be deleted
	else:

		# Node with only one child or no child
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		# Node with two children:
		# Get the inorder successor
		# (smallest in the right subtree)
		temp = minValueNode(root.right)

		# Copy the inorder successor's
		# content to this node
		root.key = temp.key

		# Delete the inorder successor
		root.right = deleteNode(root.right, temp.key)

	return root


# Driver code
""" Let us create following BST
			50
		/	 \
		30	 70
		/ \ / \
	20 40 60 80 """

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print ("Inorder traversal of the given tree")
inorder(root)

print ("\nDelete 20")
root = deleteNode(root, 20)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 30")
root = deleteNode(root, 30)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 50")
root = deleteNode(root, 50)
print ("Inorder traversal of the modified tree")
inorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
