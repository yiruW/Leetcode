# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def CompareNodes(leftN: TreeNode, rightN: TreeNode) -> bool:
            if leftN is None and rightN is not None: return False
            elif leftN is not None and rightN is None: return False
            elif leftN is None and rightN is None: return True
            elif leftN.val != rightN.val: return False
            
            leftList = CompareNodes(leftN.left, rightN.right)
            rightList = CompareNodes(leftN.right, rightN.left)
            return leftList and rightList
        
        return CompareNodes(root.left, root.right)