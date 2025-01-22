class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1
        
        def dfs(root, max_so_far):
            count = 0
            if not root:
                return 0
            
            if root.val >= max_so_far:
                count += 1
            
            count += dfs(root.left, max(root.val, max_so_far))
            count += dfs(root.right, max(root.val, max_so_far))

            return count

        return dfs(root, root.val)
    
# Time = O(n) since each node is visited once, Space = O(n) since we don't know if the tree is balanced or not