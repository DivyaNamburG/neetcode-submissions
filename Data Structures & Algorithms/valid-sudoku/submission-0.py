class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        colums = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                
                if num == '.':
                    continue
                box = (r//3) * 3 + (c//3)

                if num in rows[r]:
                    return False
                if num in colums[c]:
                    return False
                if num in boxes[box]:
                    return False
                
                rows[r].add(num)
                colums[c].add(num)
                boxes[box].add(num)
        return True