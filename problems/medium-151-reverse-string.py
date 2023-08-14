class Solution:
    def reverseWords(self, s: str) -> str:
        tokens = s.split()
        outputString = " ".join(reversed(tokens))
        return outputString