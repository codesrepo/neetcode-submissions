# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_collector = []
        if root is None:
            return level_collector
        temp = root
        stack = [(root,0)]
        while stack:
            node, level = stack.pop()
            if level == len(level_collector) and node is not None:
                level_collector.append([])
            level_collector[level].append(node.val)
            if node.right is not None:
                stack.append((node.right, level+1))
            if node.left is not None:
                stack.append((node.left, level+1))
        return level_collector
            


        