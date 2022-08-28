# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both are null
        if not p and not q:
            return True
        
        # if only one is null
        if not p or not q:
            return False
        
        # if the values are not the same
        if p.val != q.val:
            return False
        
        # check conditions for children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q