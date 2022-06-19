# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#  preorder: root, left, right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def preorderTraver(root: TreeNode):
            if root == None:
                return
            result.append(root.val)
            preorderTraver(root.left)
            preorderTraver(root.right)
            
        preorderTraver(root)
        return result
        