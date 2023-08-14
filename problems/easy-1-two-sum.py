class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {k:v for k,v in zip(nums, range(len(nums)))}
        for i, n in enumerate(nums):
            toFind = target - n
            if toFind in hashmap and i != hashmap[toFind]:
                return [i, hashmap[toFind]]
        return []