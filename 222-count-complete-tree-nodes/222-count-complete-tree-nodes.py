# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # if left and right depth is not equal: left 2 right 0 // left 1 right 0
        # if left and right depth is equal: left 2 right 1 // left 2 right 2
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if (leftDepth == rightDepth):
            return pow(2,leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)
        
    def getDepth(self, node) -> int:
        if not node:
            return 0
        return 1 + self.getDepth(node.left)