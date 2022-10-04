# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def compareTree(first: TreeNode, second: TreeNode) -> bool:
            if first is None and second is None: return True
            elif first is None and second is not None: return False
            elif first is not None and second is None: return False
            elif first.val != second.val: return False
            
            leftList = compareTree(first.left, second.left)
            rightList = compareTree(first.right, second.right)
            return leftList and rightList
        return compareTree(p, q)