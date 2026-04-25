# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        diameter = max(self.maxDepth(root.left) + self.maxDepth(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return diameter

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        depth = 1

        depth = depth + max(self.maxDepth(root.left), self.maxDepth(root.right))

        return depth