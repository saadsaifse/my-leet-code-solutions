class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isMatch(root, subRoot):
            if not root and not subRoot: # if both are null, implies equal
                return True
            if not root or not subRoot: # if one of them is null
                return False
            if root.val != subRoot.val: # if val is not equal
                return False
            leftMatch = isMatch(root.left, subRoot.left)
            return leftMatch and isMatch(root.right, subRoot.right)

        def dfs(root, subRoot):
            if not root:
                return False
            if not subRoot:
                return True
            if root.val == subRoot.val:                
                if isMatch(root, subRoot):
                    return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)