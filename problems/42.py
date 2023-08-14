from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxIndex, rightMaxIndex, i, trappedWater, highestFound, heightSecondHighest = 0, 0, 0, 0, False, 0
        while i < len(height):
            leftMaxIndex = i if height[i] >= height[leftMaxIndex] else leftMaxIndex
            heightAtLeftMaxIndex = heightSecondHighest if highestFound else height[leftMaxIndex]
            for j in range(leftMaxIndex + 1, len(height)):                    
                if height[j] >= heightAtLeftMaxIndex:
                    rightMaxIndex = j
                    break                
            if rightMaxIndex > i: # found an increasing right index
                level = min(heightAtLeftMaxIndex, height[i], height[rightMaxIndex])                
                for j in range(leftMaxIndex, rightMaxIndex):
                    trappedWater += level - height[j]
                i = rightMaxIndex
                leftMaxIndex = rightMaxIndex
                rightMaxIndex = 0
            else: # no increasing right index was found  
                if len(height) - i == 1:
                    i+=1
                    continue             
                highestFound = True
                leftMaxIndex = i + 1 + height[i+1: len(height)].index(max(height[i+1: len(height)]))
                heightSecondHighest = height[leftMaxIndex]                
                rightMaxIndex = 0
                i+=1
        return trappedWater
    

if __name__ == "__main__":
    s = Solution()
    #output = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    output = s.trap([4,2,0,3,2,5])
    print(output)