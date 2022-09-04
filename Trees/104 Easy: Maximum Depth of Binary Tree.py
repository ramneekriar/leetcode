# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            left_height = 1
            right_height = 1
            if root.left:
                left_height = 1 + self.maxDepth(root.left)
            if root.right:
                right_height = 1 + self.maxDepth(root.right)
            return max(left_height, right_height)
        else:
            return 0