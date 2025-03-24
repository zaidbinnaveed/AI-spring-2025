class CardGame:
    def __init__(self, cards):
        self.cards = cards
        self.max_score = 0
        self.min_score = 0

    def play(self):
        max_turn = True
        while self.cards:
            if max_turn:
                choice = max(self.cards[0], self.cards[-1])
                self.max_score += choice
            else:
                choice = min(self.cards[0], self.cards[-1])
                self.min_score += choice
            self.cards.remove(choice)
            max_turn = not max_turn

    def result(self):
        print(f"Final Scores - Max: {self.max_score}, Min: {self.min_score}")
        print("Winner:", "Max" if self.max_score > self.min_score else "Min")
