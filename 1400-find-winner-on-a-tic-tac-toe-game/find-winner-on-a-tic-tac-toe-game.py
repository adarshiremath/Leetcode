class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        matrix = [["" for _ in range(3)] for _ in range(3)]
        move = 0
        for r, c in moves:
            matrix[r][c] = "X" if move % 2 == 0 else "O"
            move += 1
        
        for i in range(3):
            if matrix[i][0] == matrix[i][1] and matrix[i][1] == matrix[i][2] and matrix[i][0] != "":
                return "A" if matrix[i][0]== "X" else "B"
            if matrix[0][i] == matrix[1][i] and matrix[1][i] == matrix[2][i] and matrix[0][i] != "":
                return "A" if matrix[0][i]== "X" else "B"
            
        if (matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[0][0] != "") or\
        (matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] and matrix[0][2] != ""):
            return "A" if matrix[1][1] == "X" else "B"
            
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"