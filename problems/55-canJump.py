class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        return self.canJumpRecursive(nums, 0, len(nums) - 1)

    def canJumpRecursive(self, nums, fromIndex, targetIndex) -> bool:        
        if nums[fromIndex] == 0:
            return False
        if nums[fromIndex] + fromIndex >= targetIndex:
            return True
        else:
            for i in range(fromIndex + 1, fromIndex + nums[fromIndex] + 1):
                result = self.canJumpRecursive(nums, i, targetIndex)
                if result == True:
                    return True