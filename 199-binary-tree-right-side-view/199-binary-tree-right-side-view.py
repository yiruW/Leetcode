# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root: return result
        
        def findRight(node: TreeNode, depth:int):
            if len(result) == depth: result.append([])
            result[depth] = node.val
            if node.left: findRight(node.left, depth+1)
            if node.right: findRight(node.right, depth+1)
            
                
        findRight(root, 0)
        return result