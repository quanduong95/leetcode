class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
  while root:
    if root.val > p and root.val > q:
      root = root.left
    elif root.val < p and root.val < q:
      root = root.right
    else:
      return root 
