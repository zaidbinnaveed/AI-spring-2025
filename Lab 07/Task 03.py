class Battleship:
    def __init__(self):
        self.grid_size = 10
        self.player_board = [["O"] * 10 for _ in range(10)]
        self.ai_board = [["O"] * 10 for _ in range(10)]
        self.place_ships(self.player_board)
        self.place_ships(self.ai_board)

    def place_ships(self, board):
        for _ in range(5):
            x, y = random.randint(0, 9), random.randint(0, 9)
            board[x][y] = "S"

    def attack(self, board, x, y):
        if board[x][y] == "S":
            board[x][y] = "X"
            return "Hit!"
        return "Miss"

    def ai_attack(self):
        x, y = random.randint(0, 9), random.randint(0, 9)
        return x, y, self.attack(self.player_board, x, y)
