class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                bitVal = 1 << int(board[r][c])
                sqIdx = (r // 3) * 3 + c // 3

                if (rows[r] & bitVal) or (cols[c] & bitVal) or squares[sqIdx] & bitVal:
                    return False

                rows[r] |= bitVal
                cols[c] |= bitVal
                squares[sqIdx] |= bitVal

        return True

        # grid = [[0] * 9 for _ in range(27)]

        # for r, row in enumerate(board):
        #     for c, val in enumerate(row):
        #         if val == ".":
        #             continue
        #         num = int(val)
        #         if grid[r][num - 1] != 0:
        #             return False
        #         grid[r][num - 1] = 1

        #         if grid[c + 9][num - 1] != 0:
        #             return False
        #         grid[c+9][num - 1] = 1

        #         if grid[(r // 3) * 3 + c // 3 + 18][num - 1] != 0:
        #             return False
        #         grid[(r // 3) * 3 + c // 3 + 18][num - 1] = 1

        # return True