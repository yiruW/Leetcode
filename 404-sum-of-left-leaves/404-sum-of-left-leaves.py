# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.findLeft(root, False)
        
        
    def findLeft(self, root, isLeft) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            if isLeft:
                return root.val
            else:
                return 0
        return self.findLeft(root.left, True) + self.findLeft(root.right, False)
        