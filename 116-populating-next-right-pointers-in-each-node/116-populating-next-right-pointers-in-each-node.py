"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        nodeList = []
        def levelDetect(node: Node, depth: int):
            if not node: return []
            if len(nodeList) == depth: 
                nodeList.append([])
                node.next = None
                nodeList[depth].append(node)
            else:
                node.next = nodeList[depth][len(nodeList[depth])-1]
                nodeList[depth].append(node)
            if node.right: levelDetect(node.right, depth+1)
            if node.left: levelDetect(node.left, depth+1)
        levelDetect(root, 0)
        return root