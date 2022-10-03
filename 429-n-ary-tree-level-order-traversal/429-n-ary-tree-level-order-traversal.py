"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        def levelDetect(node: 'Node', depth: int):
            if not node: return []
            if len(result) == depth: result.append([])
            result[depth].append(node.val)
            if node.children:
                for child in node.children:
                    levelDetect(child, depth+1)
        levelDetect(root, 0)
        return result