# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(self,root, subRoot):
    if not subRoot:
        return True
    if not root:
        return False

    def isSame(s, t):
        if not s and not t:
            return True
        elif s and t and s.val == t.val:
          return isSame(s.left, t.left) and isSame(s.right, t.right)
        else:
          return False
    return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
