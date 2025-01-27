import random

class CyberSecuritySystem:
    def __init__(self):
        self.components = {chr(65 + i): random.choice(["Safe", "Vulnerable"]) for i in range(9)}

    def display_system(self):
        print("System Status:")
        for component, status in self.components.items():
            print(f"Component {component}: {status}")

    def scan_and_patch(self):
        print("\nScanning the system...")
        for component, status in self.components.items():
            if status == "Vulnerable":
                print(f"Warning: Component {component} is Vulnerable.")
                self.components[component] = "Safe"
            else:
                print(f"Component {component} is Safe.")

    def run(self):
        print("Initial System Check:")
        self.display_system()

        self.scan_and_patch()

        print("\nFinal System Check:")
        self.display_system()

# Execute Task 1
task1 = CyberSecuritySystem()
task1.run()
