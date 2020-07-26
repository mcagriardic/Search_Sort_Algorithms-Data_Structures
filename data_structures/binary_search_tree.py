class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree(object):
    
    def __init__(self, root):
        self.root = root
        
    def search(self, val_to_search, root):
        if not root:
            print("Val does not exist!")
            return None
        
        if val_to_search > root.val:
            self.search(val_to_search, root.right)
        elif val_to_search < root.val:
            self.search(val_to_search, root.left)
        elif val_to_search == root.val:
            print("Val found!")
            return 1
        
    def insert(self, val_to_insert, root):
        if not root.right or not root.left:
            to_insert = TreeNode(val_to_insert)
            if val_to_insert > root.val:
                root.right = to_insert
            else:
                root.left = to_insert
            return 1
        
        if val_to_insert > root.val:
            self.insert(val_to_insert, root.right)
        elif val_to_insert < root.val:
            self.insert(val_to_insert, root.left)
            
    def delete(self, val_to_delete, root):
        # Case 1 - no child
        if not root:
            return None
        
        if val_to_delete > root.val:
            root.right = self.delete(val_to_delete, root.right)
        elif val_to_delete < root.val:
            root.left = self.delete(val_to_delete, root.left)
        elif val_to_delete == root.val:
            
            # Case 2-1 - has the left child
            if not root.right:
                return root.left
            
            # Case 2-2 - has the right child
            if not root.left:
                return root.right
            
            # Case 3 - has both childs
            if root.left and root.right:
                temp_var = root.right
                # find the minimum in the right sub tree
                while temp_var.left:
                    temp_var = temp_var.left
                
                root.val = temp_var.val
                root.right = self.delete(temp_var.val, root.right)
            
        return root
            
    def traverse(
            self,
            root,
            inorder=True,
            postorder=False,
            preorder=False
        ):

        if not root:
            return None

        if preorder:
            print(root.val)
        self.traverse(root.left)
        if inorder:
            print(root.val)
        self.traverse(root.right)
        if postorder:
            print(root.val)


### EXAMPLE ###
## Construct the tree

#                     50             
#             /                \
#            25                75
#         /      \          /      \
#        10      33        56      89
#       / \     /  \      /  \    /  \
#      4  11   30  40    52  61  82  95

##

left_1 = TreeNode(25)
right_1 = TreeNode(75)

left_1_left = TreeNode(10)
left_1_right = TreeNode(33)

left_1_left_left = TreeNode(4)
left_1_left_right = TreeNode(11)

left_1_right_left = TreeNode(30)
left_1_right_right = TreeNode(40)

right_1_left = TreeNode(56)
right_1_right = TreeNode(89)

right_1_left_left = TreeNode(52)
right_1_left_right = TreeNode(61)

right_1_right_left = TreeNode(82)
right_1_right_right = TreeNode(95)

root = TreeNode(50, left_1, right_1)

left_1.left = left_1_left
left_1.right = left_1_right

left_1_left.left = left_1_left_left
left_1_left.right = left_1_left_right

left_1_right.left = left_1_right_left 
left_1.right.right = left_1_right_right


right_1.left = right_1_left
right_1.right = right_1_right

right_1_left.left = right_1_left_left
right_1_left.right = right_1_left_right

right_1_right.left = right_1_right_left
right_1_right.right = right_1_right_right

# Test search, insert, dekete abnd traverse methods

bst = BinarySearchTree(root)
bst.search(55, root)

bst.insert(43, root)
bst.traverse(root)

root = bst.delete(50, root)
bst.traverse(root)

