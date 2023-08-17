# better solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zeroIndex = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                if zeroIndex == -1:
                    zeroIndex = i
            elif zeroIndex != -1 and nums[i] + i > zeroIndex:
                zeroIndex = -1
        return zeroIndex == -1


# not sure if the following works

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