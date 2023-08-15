# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node, values, path, res):
            if node is None:
                return None
            path.append(node)
            if node.val in values:
                res.append(path.copy())
                if len(res) == 1:
                    return res
            lP = dfs(node.left, values, path, res)
            if lP is not None:
                return res                
            while path[-1] != node:
                path.pop()
            dfs(node.right, values, path, res)
            return res


        inputvals = (p.val, q.val)
        pathQ, pathP = dfs(root, inputvals, [], [])
        # print(pathQ)        # print(pathP)

        pSet = {p.val for p in pathP}
        for qq in reversed(pathQ):
            if qq.val in pSet:
                return qq
        return 0
# [3,5]
# [3,5,2,4]

# [1]
# [1,2]



