class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        sub_boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i]:
                    return False
                row[i].add(board[i][j])

                if board[i][j] in column[j]:
                    return False
                column[j].add(board[i][j])

                i_subbox = i //3
                j_subbox = j //3

                if board[i][j] in sub_boxes[(i_subbox, j_subbox)]:
                    return False
                
                sub_boxes[(i_subbox, j_subbox)].add(board[i][j])
        return True

