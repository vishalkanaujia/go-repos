# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

ans = []
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        return self.convert(nums, 0, len(nums) - 1)
        # return ans
    
    def convert(self, nums, start, end):
        # print("nums={} start={} end={}".format(nums, start, end))
        if start > end:
            #ans.append("null")
            return None
        
        mid = start + (end - start) / 2
        
        root = TreeNode(nums[mid])
        
        root.left = self.convert(nums, start, mid - 1)
        root.right = self.convert(nums, mid + 1, end)

        # print("root={}".format(root))
        return root
    
    def preOrder(self, root):
        if not root:
            return
        
        ans.append(root.val)
        preOrder(root.left)
        preOrder(root.right)
        
        if (root.left and root.right is None) or (root.right and root.left is None):
            ans.append("null")
            