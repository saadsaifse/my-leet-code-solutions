from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        n=2
        output: ["(())", "()()"]
        output: ["(())(())", "()()()()"]

        output: ["()(())", "()()()", "(())()", "()()()", "((()))", "(()())"]

        output: ["(())", "()()", "(())", "()()"]

        Input: n = 1
        Output: ["()"]
        Output: ["()()", "(())"]

        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
        
        Output: ["()((()))", "((()))()", "(((())))",
        "()(()())","(()())()","((()()))",
        "()(())()","(())()()","((())())",
        "()()(())","()(())()","(()(()))",
        "()()()()","()()()()","(()()())"]



            ))(( -> invalid
                        ( )
            ( )                           ( ) 
    ( )             ( )           ( )             ( )
( )     ( )     ( )     ( )   ( )     ( )     ( )     ( ) 
        '''

        if n == 1:
            return ["()"]

        previous = self.generateParenthesis(n-1)
        result = []
        for i in previous:
            result.append("()" + i)
            result.append(i + "()")
            result.append(f"({i})")
        
        return result

        

# chatGPT, dynamic programming approach

class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        dp = [[] for _ in range(n + 1)]
        dp[0].append("")

        for i in range(1, n + 1):
            for j in range(i):
                left_combinations = dp[j]
                right_combinations = dp[i - j - 1]

                for left in left_combinations:
                    for right in right_combinations:
                        dp[i].append(f"({left}){right}")

        return dp[n]

# Test cases
sol = Solution1()
print(sol.generateParenthesis(3)) 
# print(sol.generateParenthesis(4))  # Output: ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
# print(sol.generateParenthesis(5))  # Output: ['((((()))))', '(((()())))', '((()(())))', '((())(()))', '((()))(())', '((())))()', '(((()))())', '((()()()))', '((())()())', '((()))()()', '((()(())))', '((())())()', '((()))(())()', '((()()())())', '((()())())()', '(((())))()', '(()((())))', '(()(()))()', '(()(())())', '(()(()())())', '(()()(()))', '(()()()())', '(()())(())', '(()())()()', '(())((()))', '(())(()())', '(())(())()', '(())()(())', '(())()()()', '()((((()))))', '()(((()())))', '()((()(())))', '()((())(()))', '()((()))(())', '()((())))()', '()(((()))())', '()((()()()))', '()((())()())', '()((()))()()', '()((()(())))', '()((())())()', '()((()))(())()', '()((()()())())', '()((()())())()', '()(((())))()', '()(()((())))', '()(()(()))()', '()(()(())())', '()(()(()())())', '()(()()(()))', '()(()()()())', '()(()())(())', '()(()())()()', '()(())(())', '()(())()()', '()()((()))', '()()(()())', '()()(())()', '()()()(())', '()()()()()']
