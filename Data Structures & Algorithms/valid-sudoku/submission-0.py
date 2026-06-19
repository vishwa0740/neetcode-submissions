class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set()for _ in range(9)]
        boxes=[set()for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    vals=board[i][j]
                    if vals in rows[i]:
                        return False 
                    if vals in cols[j]:
                        return False
                    index=(i//3)*3+(j//3)
                    if vals in boxes[index]:
                        return False
                    rows[i].add(vals)
                    cols[j].add(vals)
                    boxes[index].add(vals)
        return True