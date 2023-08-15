'''
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''
from collections import defaultdict
def lengthOfLongestSubstring(s: str) -> int:
    hashMap = defaultdict(int)
    start, end, length = 0, 0, 0
    while end < len(s):        
        hashMap[s[end]] += 1
        if hashMap[s[end]] > 1:
            while start < end and hashMap[s[end]] != 1:
                #if s[start] == s[end]:
                hashMap[s[start]] -= 1
                start+=1
        end += 1
        length = max(length, end - start)
    return length

print(lengthOfLongestSubstring("tmmzuxt"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))


def lengthOfLongestSubstring2(s: str) -> int:            
    seen = dict()
    end, length = 0, 0
    while end < len(s):
        if s[end] in seen:                
            start = seen[s[end]] + 1
            seen = {a:b for (a, b) in seen.items() if b >= start}                                
        seen[s[end]] = end              
        end += 1
        length = max(length, len(seen))
    return length