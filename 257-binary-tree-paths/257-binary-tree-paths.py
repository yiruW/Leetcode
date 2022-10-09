# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = ''
        if not root: return result
        
        def traversal(node: TreeNode, path: str, result: List[str]):
            path += str(node.val)
            if not node.left and not node.right:
                result.append(path)
            if node.left: traversal(node.left, path + '->', result)
            if node.right: traversal(node.right, path + '->', result)

        traversal(root, path, result)
        return result