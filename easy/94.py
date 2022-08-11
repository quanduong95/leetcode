class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def inorderTraversal(root):
  res =[]
  
  def inorder(node):
    if not node:
      return
    
    inorder(node.left)
    res.append(node.val)
    inorder(node.right)
    
  inorder(root)
  
  return res  

def inorderTraversal2(self,root):
  if not root:
    return []
  return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)