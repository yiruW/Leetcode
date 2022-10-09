# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def findDepth(node: TreeNode):
            if not node: return 0
            leftDepth = 1 + findDepth(node.left)
            rightDepth = 1 + findDepth(node.right)
            return max(leftDepth, rightDepth)
        
        return findDepth(root)