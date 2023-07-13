'''
Prompt:
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #we will do bfs on each tree
        p_queue = [p]
        q_queue = [q]

        if p == None and q == None: return True
        elif (p == None and q != None) or (p != None and q == None): return False 

        while len(p_queue) != 0 and len(q_queue) != 0:
            print(p_queue[0].val, q_queue[0].val)
            current_p = p_queue.pop(0)
            current_q = q_queue.pop(0)

            if current_p != None and current_q != None: #anytime we dereference a pointer we need to make sure it isnt Null / None
                if current_p.val != current_q.val:
                    return False

                if current_p.right != None and current_q.right != None:
                    p_queue.append(current_p.right)
                    q_queue.append(current_q.right)
                elif (current_p.right == None and current_q.right != None) or (current_q.right == None and current_p.right != None): return False
                # elif current_p.right == None and current_q.right == None: continue
                # else: return False

                if current_p.left != None and current_q.left != None:
                    p_queue.append(current_p.left)
                    q_queue.append(current_q.left)
                elif (current_p.left == None and current_q.left != None) or (current_q.left == None and current_p.left != None): return False
                # elif current_p.left == None and current_q.left == None: continue
                # else: return False
                    
        return True
