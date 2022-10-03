# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        def levelDetect(node: TreeNode, depth: int):
            if not node: return []
            if len(result) == depth: result.append([])
            result[depth].append(node.val)
            if node.left: levelDetect(node.left, depth+1)
            if node.right: levelDetect(node.right, depth+1)
                
        levelDetect(root, 0)
        average = []
        for i in range(len(result)):
            average.append(sum(result[i]) / len(result[i]))
            
        return average