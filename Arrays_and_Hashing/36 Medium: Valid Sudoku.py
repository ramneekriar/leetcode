import collections

class Solution:
    def validSudoku(self, board: list[list[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        blocks = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in blocks[(r //3, c //3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                blocks[(r //3, c //3)].add(board[r][c])
        return True