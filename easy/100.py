class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSameTree(self, p, q):
  if not p and not q:
    return True
  if not p or not q:
    return False
  return q.val == p.val and self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right)