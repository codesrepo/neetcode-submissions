# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:     
        stack =[]
        min_limit = -np.inf
        max_limit = np.inf
        stack.append((root, min_limit, max_limit))
        while stack:
            node = stack.pop()
            if node[0].val <= node[1] or node[0].val >= node[2]:
                return False
            
            if node[0].right is not None:   
                stack.append((node[0].right, node[0].val, node[2]))

            if node[0].left is not None:   
                stack.append((node[0].left, node[1] , node[0].val))
        return True

        