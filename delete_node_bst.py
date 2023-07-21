'''
Prompt:
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Note: needs updated with final solution, missing edgecase: if only one node in the tree.
'''

  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delete_helper(self, root, key, head):
        if root == None: return
        if key == root.val:
            print("True")
            if root.right != None:
                root.val = root.right.val
                root.right = None
            elif root.left != None:
                root.val = root.left.val
                root.left = None
            else:
                root = None
        elif key < root.val:
            #then we need to move to the left
            return self.deleteNode(root.left, key)
        elif key > root.val:
            #then we need to move to the right
            return self.deleteNode(root.right, key)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        self.delete_helper(root, key, root)
        return root
