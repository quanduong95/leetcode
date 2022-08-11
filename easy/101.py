class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymetric(root):
  
  def isMirror(l,r):
    if not l and not r:
      return True
    elif not l or not r :
      return False
    elif l.val == r.val:
      return isMirror(l.right,r.left) and isMirror(l.left,r.right)
    else:
      return False  
  return isMirror(root.l,root.r)