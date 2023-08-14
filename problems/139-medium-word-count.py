from typing import List

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)  # convert wordDict to a set for constant time lookup
    n = len(s)
    dp = [False] * (n+1)  # create an array dp of length n+1
    dp[0] = True  # empty string can be segmented into an empty sequence of words
    
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    print(dp)
    return dp[n]

# from typing import List
# # own solution
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         def isPrefix(s, word):
#             return s.startswith(word)

#         wordDict = set(wordDict)

#         def findWords(s, wordDict, memo={}):
#             if s in memo:
#                 return memo[s]

#             if len(s) == 0:
#                 return True
#             prefixWords = []
#             for word in wordDict:
#                 if isPrefix(s, word):
#                     prefixWords.append(word)

#             found = False         
#             for prefixWord in prefixWords:
#                 found = findWords(s[len(prefixWord):], wordDict)
#                 memo[s] = True
#                 if found == True:
#                     break

#             memo[s] = False
#             return found

#         return findWords(s, wordDict)



# from typing import List
# from collections import defaultdict

# class TrieNode:
#     def __init__(self):
#         self.isWord = False
#         self.child = defaultdict(TrieNode)
    
#     def addWord(self, word):
#         cur = self
#         for c in word:
#             cur = cur.child[c]
#         cur.isWord = True

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         root = TrieNode()
#         for word in wordDict:
#             root.addWord(word)
            
#         n = len(s)
#         dp = [False] * (n+1)
#         print(dp)
#         dp[n] = True
        
#         for i in range(n-1, -1, -1):
#             cur = root
#             for j in range(i+1, n+1):
#                 c = s[j-1]
#                 print(c)
#                 if c not in cur.child: break  # s[i:j] not exist in our trie
#                 cur = cur.child[c]
#                 if cur.isWord and dp[j]:
#                     dp[i] = True
#                     break
#         print(dp)
#         return dp[0]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("applepenapple", ["apple","pen", "applepenapple", 'app']))

    # t f f t f t f f t f f t f t
        