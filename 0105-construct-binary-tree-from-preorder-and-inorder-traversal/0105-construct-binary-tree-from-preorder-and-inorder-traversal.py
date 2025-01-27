#Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.preOrderIndex = 0
        self.inOrderHashmap = {}
    
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        for i, n in enumerate(inorder):
            self.inOrderHashmap[n] = i
        
        return self.buildSubTree(preorder, 0, len(inorder) - 1)
    
    def buildSubTree(self, preorder: list[int], left, right):
        if left > right:
            return None

        rootValue = preorder[self.preOrderIndex]
        root = TreeNode(rootValue)
        self.preOrderIndex += 1

        inOrderIndex = self.inOrderHashmap[rootValue]

        root.left = self.buildSubTree(preorder, left, inOrderIndex - 1)
        root.right = self.buildSubTree(preorder, inOrderIndex + 1, right)

        return root
