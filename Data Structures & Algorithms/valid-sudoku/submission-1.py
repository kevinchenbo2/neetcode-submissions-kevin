class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == '.':
                    continue
                cell = board[row][col]
                if cell in rows[row]:
                    return False
                if cell in cols[col]:
                    return False
                if cell in boxes[(row//3) * 3 + (col//3)]:
                    return False
                rows[row].add(cell)
                cols[col].add(cell)
                boxes[(row//3) * 3 + col//3].add(cell)
        return True