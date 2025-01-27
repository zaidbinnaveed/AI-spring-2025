class DeliveryRobot:
    def __init__(self):
        self.tasks = [
            {"room": f"Room {i + 1}", "medicine": random.choice(["Delivered", "Pending"])}
            for i in range(5)
        ]

    def display_tasks(self):
        print("Delivery Tasks:")
        for task in self.tasks:
            print(f"{task['room']}: Medicine {task['medicine']}")

    def complete_deliveries(self):
        print("\nCompleting deliveries...")
        for task in self.tasks:
            if task["medicine"] == "Pending":
                print(f"Delivering medicine to {task['room']}.")
                task["medicine"] = "Delivered"

    def run(self):
        print("Initial Task Status:")
        self.display_tasks()

        self.complete_deliveries()

        print("\nFinal Task Status:")
        self.display_tasks()

# Execute Task 5
task5 = DeliveryRobot()
task5.run()
