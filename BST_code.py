# Create a Binary Search Tree class
class BSTNode:
	# construction of the class
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        
    # search the value in the tree
    def search(self, val):
        # Found the value in the tree
        if val == self.val:
            return True
        # The value is less than the current node
        if val < self.val:
            if self.left == None:
                return False
            return self.left.search(val)
        # The value is more than the current node
        else:
            if self.right == None:
                return False
            return self.right.search(val)
  
	# Insert a value
    def insert(self, val):
		# Set the root node when the tree is empty
        if not self.val:
            self.val = val
            return
            
		# Check when insert the value that the tree already has
        if self.val == val:
            print('The tree already has the value {}'.format(val))
            return
            
        # The value is less than the current node
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
            
        # The value is more than the current node
        else:
            if self.right:
                self.right.insert(val)
                return
            self.right = BSTNode(val)

    # Find the minimum value 
    def get_min(self):
        current = self
        while current.left:
            current = current.left
        return current.val

    # Find the maximum value
    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.val

    # Return all values in the tree in order to their keys
    def inorder(self, vals):
        if self.left:
            self.left.inorder(vals)
        if self.val:
            vals.append(self.val)
        if self.right:
            self.right.inorder(vals)
        return vals

    # Delete a value from the tree
    def delete(self, val):
        # The value is equal to a current node
        if (self.val == val):
            # The current node has left and right subtree
            if self.left and self.right:
                min_larger_node = self.right
                while min_larger_node.left:
                    min_larger_node = min_larger_node.left
                self.val = min_larger_node.val
                self.right = self.right.delete(min_larger_node.val)
            # The current node has either left or right subtree
            else:
                if self.right == None:
                    return self.left
                if self.left == None:
                    return self.right
        # The value is not equal to a current node
        else:
            if val < self.val:
                if self.left:
                    self.left = self.left.delete(val)
                return self
            if val > self.val:
                if self.right:
                    self.right = self.right.delete(val)
                return self
        return self
        
    #Return all values in order to their keys without using recursion
    def inorder_noRecursion(self, vals):
        stack = []
        while True:
            if self is not None:
                stack.append(self)
                self = self.left
            elif stack:
                self = stack.pop()
                vals.append(self.val)
                self = self.right
            else:
                return vals
                

if __name__ == '__main__':
    # All values in the tree
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    # Create a Binary Search Tree
    bst = BSTNode()
    
    # Add all values to the tree
    for num in nums:
        bst.insert(num)
    
    # Search the node that has value 4
    print("Does 4 exist in the tree?")
    if bst.search(4):
        print('Found 4 in the tree')
    else:
        print('Not found 4 in the tree')
    # Search the node that has value 18
    print("Does 18 exist in the tree?")
    if bst.search(18):
        print('Found 18 in the tree')
    else:
        print('Not found 18 in the tree')
        
    # Find the min and max values in the tree
    print('The minimum value in the tree is {}'.format(bst.get_min()))
    print(bst.get_min())
    print('The maximum value in the tree is {}'.format(bst.get_max()))
    print(bst.get_max())

    # Show all in-order values in the tree
    print("The in-order values in the tree:")
    print(bst.inorder([]))

    # Delete the values in the list
    nums = [2, 18, 20]
    print("deleting " + str(nums))
    for num in nums:
        bst.delete(num)
    
    # Show all in-order values in the tree (non-recursion)
    print("The in-order values in the tree (non-recursion): ")
    print(bst.inorder_noRecursion([]))







# print("12 exists:")
# print(bst.exists(12))
# print("18 exists:")
# print(bst.exists(18))

https://qvault.io/python/binary-search-tree-in-python/
https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
https://stackoverflow.com/questions/33448561/delete-node-in-binary-search-tree-python/33449471
https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/