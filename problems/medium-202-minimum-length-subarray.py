class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:        
        start, end, length = 0, 0, float('inf')
        sum = 0
        while end < len(nums):
            sum += nums[end]
            while sum >= target:
                length = min(length, end - start + 1)
                sum -= nums[start]
                start+=1
            end += 1            
        return length if length <= len(nums) else 0