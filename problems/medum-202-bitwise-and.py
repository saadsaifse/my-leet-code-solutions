#chatGPT solution

def range_bitwise_and(left, right):
    # Initialize a shift variable to 0
    shift = 0

    # Keep right shifting the numbers until they are equal
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1

    # After the loop, left and right will have the common prefix
    # Shift it back to get the final result
    return left << shift

# Test cases
print(range_bitwise_and(9, 12))        
print(range_bitwise_and(5, 7))          # Output: 4
print(range_bitwise_and(0, 0))          # Output: 0
print(range_bitwise_and(1, 214))
                

'''
Elena's sol

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        5       6   7
        8421   8421  8421   
        0101   0110  0111

        0101 + 0110 + 0111 = 0100 = 4
        5 & 7 -> 0101 -> [0,2] (list of indices that are 1, starting right to left)
        5+2^0 = 6 is in the list --> remove 0 from index list
        5+2^2 = 9 is not in the list --> return 2^2 = 4

        # get list of indices
        binrepr = str(bin(left & right))
        print(binrepr)
        # example: 0b1001001100
        # --> [2, 3, 6, 9] list of indices
        indices = [len(binrepr) - 1 - i for i, b in enumerate(binrepr) if b == "1"]
        indices.sort()

        while len(indices) > 0:
            print(indices)
            first = indices[0]
            print(first, left + 2 ** first) # 0b1001001100 + 0b100 (==2 ** 2) [0b1001010000]
            if left + 2 ** first <= right:
                indices.pop(0)
            else:
                break
        
        return (sum([2 ** i for i in indices]))


        # if left == right:
        #     return left
        # if left == 0 or right == 0:
        #     return 0
        # result = left
        # for num in range(left + 1, right+1):
        #     binaryStr = bin(num)
        #     binStr
        #     result = result & num
        #     if result == 0:
        #         return result            
        # return result


        # if left == right:
        #     return left
        # if left == 0 or right == 0:
        #     return 0
        # result = left
        # for num in range(left + 1, right+1):            
        #     result = result & num
        #     if result == 0:
        #         return result            
        # return result





'''