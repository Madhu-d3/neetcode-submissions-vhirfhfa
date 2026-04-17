class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        column_map = defaultdict(set)
        block_map = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] =='.':
                    continue
                if (board[r][c] in row_map[r] or
                    board[r][c] in column_map[c] or
                    board[r][c] in block_map[(r//3,c//3)] ):
                    return False
                row_map[r].add(board[r][c])
                column_map[c].add(board[r][c])
                block_map[(r//3,c//3)].add(board[r][c])
        return True