class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        result = []

        def solve(currentCombination, candidates, target, loop_end):
            if target == 0:
                return currentCombination
            if len(candidates) == 0:
                return

            element = candidates[0]
            maxNoElements = target // element
    
            combination = []
            for noElements in range(maxNoElements, loop_end,-1):
                combination = [element] * noElements
                # print(combination)
                newTarget = target - element * noElements
                # print(f"newTarget: {newTarget}")
                res = currentCombination.copy()
                res.extend(combination)
                # 2,2,2 | 3,6,7 | 1
                # 2,2 | 3,6,7 | 1
                newCombination = solve(res, candidates[1:], newTarget, -1)                  
                # print(newCombination)       
                if newCombination:
                    result.append(newCombination)

            
        for i in range(len(candidates)):
            solve([], candidates[i:], target, 0)

        return result



        # print(candidates, target)
        # if len(candidates) == 1:
        #     if target < candidates[0]:
        #         return []          
        #     return [candidates[0]] * (target // candidates[0])
        
        # result = []
        # for i in range(len(candidates)):
        #     firstElement = candidates[0]
        #     combination = [firstElement] * (target // firstElement)
        #     newTarget = target - firstElement * len(combination)
            


        # firstElement = candidates[0]
        # combination = []
        # for i in range(target // firstElement, -1,-1):
        #     combination = [firstElement] * i
        #     print(combination)
        #     newTarget = target - firstElement * i
        #     if newTarget == 0:
        #         return combination + [firstElement]
        #     print(f"newTarget: {newTarget}")
        #     combination2 = self.combinationSum(candidates[1:], target - firstElement * i)
        #     print(combination2)
        #     combination = combination + combination2
        # return combination
        

        
        
        

        
        '''
        take the number
        '''