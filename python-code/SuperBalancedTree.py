'''
Write a function to see if a binary tree ↴ is "superbalanced" (a new tree property we just made up).

A tree is "superbalanced" if the difference between the depths of any two leaf nodes ↴ is no greater than one.
'''
'''
solution algorithm:
 recursively traverse tree with trackers
 for max leaf depth and min leaf depth
 if max-min > 1 tree is not superbalanced
 if tree is completely traversed and max-min <=1 return balanced
 use DFS (depth first search) bc more likely to hit leaves quickly and short circuit
'''

class BinaryTreeNode:
  def __init__ (self, value):
    self.value = value
    self.left = None
    self.right = None

  def insertLeft(self, value):
    self.left = BinaryTreeNode(value)
    return self.left

  def insertRight(self, value):
    self.right = BinaryTreeNode(value)
    return self.right

def isBalanced(root):
  if root is None:
    return True

  depths = []
  nodes  = []
  nodes.append((root, 0))
  while len(nodes):
    node, depth = nodes.pop()
    if (not node.left) and (not node.right):
      if depth not in depths:
        depths.append(depth)

        if ((len(depths) > 2) or (len(depths)== 2 and abs(depths[0]-depths[1])>1)):
          return False
    else:
      if node.left:
        nodes.append((node.left, depth+1))
      if node.right:
        nodes.append((node.right, depth+1))
  return True

rootA = BinaryTreeNode(1)
rootA.insertLeft(BinaryTreeNode(2))
print isBalanced(rootA)

b = BinaryTreeNode(1)
b.left = BinaryTreeNode(2)
b.right = BinaryTreeNode(3)
b.left.left = BinaryTreeNode(4)
b.left.left.left = BinaryTreeNode(5)
print isBalanced(b)