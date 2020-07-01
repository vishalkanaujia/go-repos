# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

preWalk = []
postWalk = []

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        if root.left is None and root.right is None:
            return True
        
        if root.left is not None and root.right is not None:
            if root.left.val != root.right.val:
                return False
        
        self.preOrder(root.left)    
        self.postOrder(root.right)
        
        #print(preWalk, postWalk)
        for i,j in zip(preWalk, postWalk):
            if i != j:
                return False
        
        return True
        
    def preOrder(self, root):
        if root == None:
            preWalk.append("null")
            return
        
        preWalk.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
            
    def postOrder(self, root):
        if root == None:
            postWalk.append("null")
            return
        
        postWalk.append(root.val)

        self.postOrder(root.right)
        self.postOrder(root.left)

''' Two tree based O(1) solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

preWalk = []
postWalk = []

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        return self.isMirror(root, root)
    
    def isMirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        
        if root1 is not None and root2 is not None:
            if root1.val == root2.val:
                isMirror1 = self.isMirror(root1.left, root2.right)
                isMirror2 = self.isMirror(root1.right, root2.left)
                return isMirror1 and isMirror2
    
        return False
'''