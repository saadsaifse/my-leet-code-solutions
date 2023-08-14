
# Elena's solution

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {}
        letters[2] = "abc"
        letters[3] = "def"
        letters[4] = "ghi"
        letters[5] = "jkl"
        letters[6] = "mno"
        letters[7] = "pqrs"
        letters[8] = "tuv"
        letters[9] = "wxyz"

        
        def createCombinations(digits) -> List[str]:
            if len(digits) == 0:
                return []

            sub_solution = createCombinations(digits[1:])
            firstDigit = int(digits[0])
            result = createDotProduct(sub_solution, list(letters[firstDigit]))
            return result

        def createDotProduct(list1, singles):
            if len(list1) == 0:
                return singles
            result = []
            for i, letter in enumerate(singles):
                n = [letter] * len(list1)
                newCombinations = [f"{x}{y}" for x, y in zip(n, list1)]        
                result.extend(newCombinations)
            return result
                
        return createCombinations(list(digits))




# Saad's init approach (not working 100%)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {}
        letters[2] = "abc"
        letters[3] = "def"
        letters[4] = "ghi"
        letters[5] = "jkl"
        letters[6] = "mno"
        letters[7] = "pqrs"
        letters[8] = "tuv"
        letters[9] = "wxyz"

        def createCombinations(digits, result):
            if len(digits) == 0:
                return result # []
            if len(result) == 0:
                result = list(letters[int(digits[0])])
                return createCombinations(digits[1:], result)
                      
            firstDigit = int(digits[0])
            
            currentCombinationsLength = len(result)  
            finalResult = []          
            for i, letter in enumerate(letters[firstDigit]):
                n = [letter] * currentCombinationsLength
                print(n)
                print(result)  
                newCombinations = [f"{x}{y}" for x, y in zip(result, n)]        
                print(newCombinations)
                result.extend(newCombinations)
                if len(digits) == 1:
                    finalResult.extend(newCombinations)                
                    print(finalResult)
            
            if len(digits) == 1:
                result = finalResult
                print(finalResult)

            return createCombinations(digits[1:], result)
                
        return createCombinations(digits, [])

'''
"234" == "23" + "4"
--> use l== output for "23" and combine it with "4" = ["g", "h", "i"]
["adg","aeg","afg","bdg","beg","bfg","cdg","ceg","cfg"].ext
end
["ad","ae","af","bd","be","bf","cd","ce","cf"]


["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", ... ]
'''

        