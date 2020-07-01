# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

height = 0
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        height =  max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        
        return height