import random

class Checkers:
    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]
        self.init_board()

    def init_board(self):
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = -1
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = 1

    def display(self):
        for row in self.board:
            print(row)
        print()

    def move_piece(self, start, end):
        r1, c1 = start
        r2, c2 = end
        if abs(r2 - r1) == 2 and abs(c2 - c1) == 2:
            self.board[(r1 + r2) // 2][(c1 + c2) // 2] = 0
        self.board[r2][c2], self.board[r1][c1] = self.board[r1][c1], 0

    def ai_move(self):
        moves = self.get_moves(-1)
        if moves:
            move = random.choice(moves)
            self.move_piece(move[0], move[1])

    def get_moves(self, player):
        moves = []
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == player:
                    directions = [(-1, -1), (-1, 1)] if player == 1 else [(1, -1), (1, 1)]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < 8 and 0 <= nc < 8 and self.board[nr][nc] == 0:
                            moves.append(((r, c), (nr, nc)))
        return moves
