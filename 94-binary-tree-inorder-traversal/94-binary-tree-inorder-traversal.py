# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorderTraversal(root: TreeNode):
            if root == None:
                return
            inorderTraversal(root.left)
            result.append(root.val)
            inorderTraversal(root.right)
            
        inorderTraversal(root)
        return result