# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack=[root]
        parent=[-1]*101
        parent[root.val]=root
        while stack:
            node = stack.pop()
            if node.right is not None:
                parent[node.right.val] = node
                stack.append(node.right)
            if node.left is not None:
                parent[node.left.val] = node
                stack.append(node.left)
        
        qparents = [q]
        while parent[qparents[-1].val].val!=root.val:
            qparents.append(parent[qparents[-1].val])
        qparents.append(root)

        pparents = [p]
        while parent[pparents[-1].val].val!=root.val:
            pparents.append(parent[pparents[-1].val])
        pparents.append(root)

        for i in pparents:
            for j in qparents:
                if i.val==j.val:
                    return i



        

        