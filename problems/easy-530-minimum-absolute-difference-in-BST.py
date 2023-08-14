from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minimumDifferences = []
        seen = set()

        def findMinimumDifferences(node, value):
            if not node:
                return
            seen.add(value)
            leftDiff, rightDiff = None, None
            if node.left:
                leftDiff = abs(value - node.left.val)
            if node.right:
                rightDiff = abs(value - node.right.val)

            if leftDiff and rightDiff:
                minimumDifferences.append(min(leftDiff, rightDiff))
            elif leftDiff:
                minimumDifferences.append(leftDiff)
            elif rightDiff:
                minimumDifferences.append(rightDiff)
        
            if node.left:
                findMinimumDifferences(node.left, value)
            if node.right:
                findMinimumDifferences(node.right, value)
            
            if node.left and node.left.val not in seen:
                findMinimumDifferences(node.left, node.left.val)
            if node.right and node.right.val not in seen:
                findMinimumDifferences(node.right, node.right.val)
            
           
        findMinimumDifferences(root, root.val)
        return min(minimumDifferences) if len(minimumDifferences) > 0 else 0