# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def levelDetect(node: TreeNode, depth: int):
            if not node: return
            if len(result) == depth: result.insert(0, [])
            result[len(result) - depth - 1].append(node.val)
            if node.left: levelDetect(node.left, depth+1)
            if node.right: levelDetect(node.right, depth+1)
            
        levelDetect(root, 0)
        return result