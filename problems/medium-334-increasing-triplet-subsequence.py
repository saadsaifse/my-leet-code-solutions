class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minSeen = float('inf')
        secondMin = float('inf')
        for n in nums:
            if n <= minSeen:
                minSeen = n
            elif n <= secondMin:
                secondMin = n
            elif n > secondMin:
                return True
        return False