# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def traverseZigZag(node, nextDirection, memo):            
            if node is None:
                return 0
            if nextDirection is None:
                return max(traverseZigZag(node.right, 'l', memo), traverseZigZag(node.left, 'r', memo))
            if (id(node), nextDirection) in memo:
                return memo[(id(node), nextDirection)]
            if nextDirection == 'l' and node.left:
                res = traverseZigZag(node.left, 'r', memo) + 1
                memo[(id(node.left), 'r')] = res
                return res
            elif nextDirection == 'r' and node.right:
                res = traverseZigZag(node.right, 'l', memo) + 1
                memo[(id(node.right), 'l')] = res
                return res
            else:
                return 1   

        def traverseAll(node, lengths, memo):
            if node is None:
                return 0
            lengths.append(traverseZigZag(node, None, memo))
            traverseAll(node.left, lengths, memo)
            traverseAll(node.right, lengths, memo)            
        memo = {}
        lengths = []
        traverseAll(root, lengths, memo)
        return max(lengths)
    

    # much better solution on LC

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0

        def dfs(node, left, right):
            self.maxi = max(self.maxi, left, right)

            if node.left:
                dfs(node.left, right + 1, 0)

            if node.right:
                dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)
        return self.maxi