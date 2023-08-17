class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def move(fromM, fromN, m, n, memo):
            if fromN >= n or fromM >= m:
                return 0
            if memo.get(f'{fromM}.{fromN}'):
                print('getting from memo')
                return memo[f'{fromM}.{fromN}']
            if fromM == m - 1 and fromN == n - 1:
                print('at goal')
                return 1
            moveRight = move(fromM, fromN + 1, m, n, memo)
            moveDown = move(fromM + 1, fromN, m, n, memo)
            memo[f'{fromM}.{fromN}'] = moveRight + moveDown
            print('right', moveRight)
            print('down', moveDown)
            print(memo)
            return moveRight + moveDown
        return move(0, 0, m, n, memo)

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(3,7))
