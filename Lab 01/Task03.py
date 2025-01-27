class BackupManager:
    def __init__(self):
        self.tasks = [random.choice(["Completed", "Failed"]) for _ in range(10)]

    def display_tasks(self):
        print("Backup Task Status:")
        for i, status in enumerate(self.tasks, 1):
            print(f"Task {i}: {status}")

    def retry_failed_tasks(self):
        print("\nRetrying failed backups...")
        for i, status in enumerate(self.tasks):
            if status == "Failed":
                print(f"Retrying Task {i + 1}... Success!")
                self.tasks[i] = "Completed"

    def run(self):
        print("Initial Task Status:")
        self.display_tasks()

        self.retry_failed_tasks()

        print("\nFinal Task Status:")
        self.display_tasks()

# Execute Task 3
task3 = BackupManager()
task3.run()
