class FirefightingRobot:
    def __init__(self):
        self.grid = [
            "Safe", "Safe", "Fire",
            "Safe", "Fire", "Safe",
            "Safe", "Safe", "Fire"
        ]
        self.path = [i for i in range(9)]

    def display_grid(self):
        print("\nBuilding Status:")
        for i in range(0, 9, 3):
            print(" | ".join(self.grid[i:i + 3]))

    def extinguish_fire(self):
        print("\nFirefighting in progress...")
        for pos in self.path:
            if self.grid[pos] == "Fire":
                print(f"Extinguishing fire in Room {chr(97 + pos).upper()}.")
                self.grid[pos] = "Safe"

    def run(self):
        print("Initial Building Status:")
        self.display_grid()

        self.extinguish_fire()

        print("\nFinal Building Status:")
        self.display_grid()

# Execute Task 6
task6 = FirefightingRobot()
task6.run()
