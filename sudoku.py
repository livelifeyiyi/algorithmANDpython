from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # Double-check basic assumptions
        if ( len(board) != 9 ):
            return False

        if ( len(board[0]) != 9 ):
            return False

        def validBoardPiece(numSet):
            dict = defaultdict(int)

            for numChar in numSet:
                dict[numChar] += 1

            for number, amount in dict.items():
                if (number != '.' and amount > 1):
                    return False

            return True

        # Check Rows
        for row in board:
            if (not validBoardPiece(list(row))):
                return False

        # Check Columns
        for columnIndex in range(9):
            column = []
            for rowIndex in range(9):
                column.append(board[rowIndex][columnIndex])

            if (not validBoardPiece(list(column))):
                return False

        # Check Squares
        for boxY in range(3):
            for boxX in range(3):
                box = []
                for x in range(3):
                    for y in range(3):
                        box.append( board[(boxY*3) + y][(boxX*3) + x] )

                if (not validBoardPiece(list(box))):
                    return False

        return True
        

class Solution2(object):
def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    map_row = [{} for _ in xrange(9)]
    map_col = [{} for _ in xrange(9)]
    map_cell = [[{} for _ in xrange(3)] for __ in xrange(3)]
    for i in xrange(9):
        for j in xrange(9):
            char = board[i][j]
            if char == '.': continue
            if char in map_row[i]: return False
            else: map_row[i][char] = [i,j]
            if char in map_col[j]: return False
            else: map_col[j][char] = [i,j]
            if char in map_cell[i/3][j/3]: return False
            else: map_cell[i/3][j/3][char] = [i,j]
    return True