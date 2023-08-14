class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer <= rightPointer:
            left = s[leftPointer].lower()
            right = s[rightPointer].lower()
            
            if not left.isalnum():
                leftPointer += 1
                continue
            if not right.isalnum():
                rightPointer -= 1
                continue            
            
            if left != right:
                return False

            leftPointer += 1
            rightPointer -= 1
            
        return True  