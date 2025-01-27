class LoadBalancer:
    def __init__(self):
        self.servers = [random.choice(["Underloaded", "Balanced", "Overloaded"]) for _ in range(5)]

    def display_load(self):
        print("Server Load Status:")
        for i, status in enumerate(self.servers, 1):
            print(f"Server {i}: {status}")

    def balance_load(self):
        print("\nBalancing the load...")
        overloaded = [i for i, load in enumerate(self.servers) if load == "Overloaded"]
        underloaded = [i for i, load in enumerate(self.servers) if load == "Underloaded"]

        for o in overloaded:
            if underloaded:
                u = underloaded.pop()
                print(f"Moving tasks from Server {o + 1} to Server {u + 1}")
                self.servers[o] = "Balanced"
                self.servers[u] = "Balanced"

    def run(self):
        print("Initial Server Load:")
        self.display_load()

        self.balance_load()

        print("\nFinal Server Load:")
        self.display_load()

# Execute Task 2
task2 = LoadBalancer()
task2.run()
