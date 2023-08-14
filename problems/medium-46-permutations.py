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


        
