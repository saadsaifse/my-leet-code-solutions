class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numsLength = len(nums)
        leftIndex = 0
        rightIndex = numsLength - 1
        output = 0

        if numsLength == 1 and nums[0] == val:
            del nums[0]
            return 0


        while leftIndex <= rightIndex:
            rightIndexVal = nums[rightIndex]
            if rightIndexVal == val:                
                output += 1
            else:
                for i in range(leftIndex, rightIndex):
                    if nums[i] != val:                        
                        continue
                    else:
                        temp = nums[rightIndex]
                        del nums[rightIndex]
                        #nums[rightIndex] = nums[i]
                        nums[i] = temp
                        leftIndex = i + 1
                        output += 1
                        break
            rightIndex -= 1  
        return numsLength - output

                    
## much better solution already exists

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
        
        

