# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def countSum(node: TreeNode):
            if not node: return 0
            leftSum = countSum(node.left)
            rightSum = countSum(node.right)
            treeSum = leftSum + rightSum + 1
            return treeSum
        return countSum(root)