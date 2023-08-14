from typing import List

def rob(nums: List[int]) -> int:
    res = dict()
    def rob_efficient(nums: List[int], index : int):
        if index in res:
            return
        if index >= len(nums):
            res[index] = 0
        elif index == len(nums) - 1:
            res[index] = nums[-1]
        else:
            rob_efficient(nums, index + 2)
            rob_efficient(nums, index + 3)
            res[index] = max(nums[index] + res[index+2],\
                            nums[index + 1] + res[index + 3])
    rob_efficient(nums, 0)
    return res[0]

print(rob([1,2,1,3,100]))
# print(rob([2,7,9,3,1]))