from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = end = nums[0]
        output = []

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start != end: output.append(f"{start}->{end}") 
                else: output.append(str(start))
            
                start = end = nums[i]

        if start != end: output.append(f"{start}->{end}")
        else: output.append(str(start))

        return output
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.summaryRanges([0,1,2,4,5,7]))
    print(sol.summaryRanges([0,2,3,4,6,8,9]))