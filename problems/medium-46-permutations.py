class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ''''
        [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        [[1], [2], [1,2], [2,1]]

        [1,2] = [[1,2], [2,1]]
        [1] [2]

        [2], [1]

        
        [[1,2,3,4],[1,2,4,3],[1,4,3,2] [2,1,3],[2,3,1],[3,1,2],[3,2,1]]

        [1,2] = [[1,2], [2,1]]
        [1,3] = [[1,3], [3,1]]
        [2,3] = [[2,3], [3,2]]

        [1,2,3] = [[1,2,3], [1,3,2], [3,1,2], [2,1,3], [2,3,1], [3,2,1]]

        [1,2,3,4] = [[1,2,3,4], [1,2,4,3], [1,4,2,3], [4,1,2,3], 
                     [2,1,3,4], [2,1,4,3], [2,4,1,3], [4,2,1,3],
                      ]

        '''

        if len(nums) == 1:
            return [nums]

        result = []
        for i in range(len(nums)):
            first = [nums[i]]
            remaining = nums[:i] + nums[i+1:]
            remainingPermutations = self.permute(remaining)            

            for perm in remainingPermutations:
                result.append(first + perm)
            
        return result 
    


# another way

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


        
