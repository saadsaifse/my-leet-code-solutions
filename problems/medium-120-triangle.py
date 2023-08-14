from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:        

        def subTriangleMinTotal(level, position, triangle, memo):
            if level == len(triangle) - 1:
                return triangle[level][position]
            if (level, position) in memo:
                return memo[(level, position)]        
            # if triangle[level+1][position] < triangle[level+1][position+1]):
            memo[(level, position)] = triangle[level][position] + min(subTriangleMinTotal(level + 1, position, triangle, memo), subTriangleMinTotal(level+1, position+1, triangle, memo))
            return memo[(level, position)]        

        return subTriangleMinTotal(0, 0, triangle, {})
            
