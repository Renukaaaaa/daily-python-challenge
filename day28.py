
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        def mirror(t1, t2):
            if not t1 and not t2: return True
            if not t1 or not t2: return False
            return t1.val == t2.val and mirror(t1.left, t2.right) and mirror(t1.right, t2.left)
        return not root or mirror(root.left, root.right)

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

sol = Solution()
print(sol.isSymmetric(root))  
