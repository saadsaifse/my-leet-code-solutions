# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import groupby
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        d = defaultdict(int)
        def bfs(queue):
            if not queue or not queue[-1]:
                return

            item = queue.pop()
            node = item[0]
            lvl = item[1]

            if node is None:
                return
            
            d[lvl] = node.val

            if node.left:
                queue.insert(0, (node.left, lvl + 1))
            if node.right:
                queue.insert(0, (node.right, lvl + 1))

            bfs(queue)
        
        queue.insert(0, (root, 1))
        bfs(queue)

        return list(d.values())

            
            
