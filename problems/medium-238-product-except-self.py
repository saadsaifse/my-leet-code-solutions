from typing import List

# dynamic programming approach
class Solution:
# dynamic programming approach
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize left and right arrays
        left_products = [1] * n
        right_products = [1] * n
        
        # Calculate products to the left of each element
        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]
        
        # Calculate products to the right of each element
        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
        
        # Multiply left and right products to get the final result
        answer = [left_products[i] * right_products[i] for i in range(n)]
        
        return answer
    
# dynamic programming approach with space optimization

    def productExceptSelf_space_optimized(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        answer[0] = 1
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
        
        rightProduct = 1
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * rightProduct
            rightProduct *= nums[i]
        
        return answer

    