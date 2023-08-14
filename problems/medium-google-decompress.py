'''
In this exercise, you're going to decompress a compressed string.

Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

The input

3[abc]4[ab]c

Would be output as

abcabcabcababababc

Other rules

Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

Characters allowed as input include digits, small English letters and brackets [ ].

Digits are only to represent amount of repetitions.

Letters are just letters.

Brackets are only part of syntax of writing repeated substring.

Input is always valid, so no need to check its validity.

Learning objectives

This question gives you the chance to practice with strings, recursion, algorithm, compilers, automata, and loops. It’s also an opportunity to work on coding with better efficiency.
'''

def decompress(str):
    if not str:
        return ''
    
    if not '[' in str:
        return str

    decompressionStartIndex = 0
    decompressionEndIndex = 0
    repeatingStartIndex = 0
    repeatingEndIndex = 0
    repeatingFactor = 1
    openBracketCount = 0

    for i, c in enumerate(str):
        if c == '[':
            openBracketCount += 1
            repeatingStartIndex = i+1
            j = i-1  
            factor = ""
            while True:
                try:
                    num = int(str[j])
                    factor = f"{num}" + factor
                    j -= 1
                except:
                    break
            repeatingFactor = int(factor)
            repeatingFactor = int(repeatingFactor)            
            decompressionStartIndex = j + 1            
            break
    
    for i in range(repeatingStartIndex, len(str)):
            if str[i] == '[':
                openBracketCount += 1
            if str[i] == ']':
                 openBracketCount -= 1
                 if openBracketCount == 0:
                    decompressionEndIndex = i
                    repeatingEndIndex = i-1
                    break
        
    subString = str[repeatingStartIndex:repeatingEndIndex+1]   
    subString = subString * repeatingFactor

    return str[:decompressionStartIndex] + decompress(subString) + decompress(str[decompressionEndIndex+1:])
    

testCase = "2[3[a]b]"
output = "aaabaaab"


testCase1 = "aa3[a]bhy4[y]z"
output = "aaaaabhyyyyyz"

testCase2 = "aa2[3[a]bh]yyz"
 
actualOutput = decompress(testCase2)
print(actualOutput)



# first approach (not working)

# def decompress(str):
#     if len(str) == 0:    
#         return
#     print(str)
#     s =  ""
#     result = ""
#     for i, c in enumerate(str):
#         if c == '[':
#             repeatingFactor = ''
#             for j in range(i):
#                 repeatingFactor += str[j]
#             repeatingFactor = int(repeatingFactor)
#             print(repeatingFactor)
#             subString = decompress(str[i+1:])
#             print(subString)
#             for i in range(repeatingFactor):
#                 result = result + subString
#             continue
#         if c != ']':
#             continue
#         if c == ']':
#             return s


