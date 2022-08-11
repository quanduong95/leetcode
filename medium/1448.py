class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def goodNodes(self, root: TreeNode) -> int:
  def nextNode(node,maxVal):
    if not node:
      return 0
    res = 1 if node.val >= maxVal else 0
    maxVal = max(node.val,maxVal)
    res += nextNode(node.left,maxVal)
    res += nextNode(node.right,maxVal)
    return res
  
  return nextNode(root,root.val)