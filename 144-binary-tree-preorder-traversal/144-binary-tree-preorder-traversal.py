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
        def preOrder(node):
            if node == None:
                return
            result.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)
        return result
        