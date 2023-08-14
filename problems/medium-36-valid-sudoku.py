from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkSubBoard(subBoard):
            seen = set()
            isValid = all(value not in seen and seen.add(value) is None for row in subBoard for value in row if value != ".")
            return isValid
            # above is the list comprehension that achieves the same as below code
            # print(integerValues)
            # for row in subBoard:
            #     for value in row:
            #         if value in seen and value != ".":
            #             return False
            #         seen.add(value)
            # return True

        def checkList(elements):
            seen = set()
            isValid = all(value not in seen and seen.add(value) is None for value in elements if value != ".")
            return isValid
            # for value in elements:           
            #     if value in seen and value != ".":
            #         return False
            #     seen.add(value)
            # return True        

        invalidSubBoard = any(checkSubBoard([row[j:j+3] for row in board[i:i+3]]) is False for i in range(0,9,3) for j in range(0,9,3))        
        if invalidSubBoard:
            return False
        # for i in range(0,9,3):
        #     for j in range(0,9,3):
        #         subBoard = [row[j:j+3] for row in board[i:i+3]]
        #         if not checkSubBoard(subBoard):                    
        #             return False

        rowSeen = dict()
        columnSeen = dict()
        for i, row in enumerate(board):          
            for j, value in enumerate(row):
                if value == '.':
                    continue
                else:
                    if i not in rowSeen:
                        if not checkList(row):
                            return False                            
                        rowSeen[i] = i
                    if j not in columnSeen:
                        if not checkList(board[:][j]):
                            return False
                        columnSeen[j] = j
        return True


        
if __name__ == "__main__":
    sol = Solution()
    board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    
    board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


    print(sol.isValidSudoku(board1))
    print(sol.isValidSudoku(board2))