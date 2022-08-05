
def invertTree(self, root):
  if root is None:
    return root
  temp = root.right
  root.right = root.left
  root.left = temp
  self.invertTree(root.left)
  self.invertTree(root.right)
  return root
  