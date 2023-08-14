import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        element = 0 
        if k > 0 and k < len(nums)//2:
            nums = [-x for x in nums]
            heapq.heapify(nums)
            for _ in range(k):
                element = heapq.heappop(nums)
                
            return element * -1 

        else:
            heapq.heapify(nums)
            for _ in range(len(nums) - k + 1):
                element = heapq.heappop(nums)
            return element