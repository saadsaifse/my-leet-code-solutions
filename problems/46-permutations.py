from typing import List

class Solution:
    def backtrack(self, list: List[List[int]], tempList: List[int], nums: List[int]):
        if(len(tempList) == len(nums)):
            list.append(tempList[:])
        else:
            for i in range(0, len(nums)):
                if nums[i] in tempList: 
                    continue
                tempList.append(nums[i])
                self.backtrack(list, tempList, nums)
                tempList.pop()

    def permute(self, nums):
        list = []   
        self.backtrack(list, [], nums)
        return list

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1,2,3,4]))