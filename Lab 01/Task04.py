class SecurityAgent:
    def __init__(self):
        self.components = {chr(65 + i): random.choice(["Safe", "Low Risk", "High Risk"]) for i in range(9)}

    def display_system(self):
        print("System Status:")
        for component, status in self.components.items():
            print(f"Component {component}: {status}")

    def patch_system(self):
        print("\nScanning and patching...")
        for component, status in self.components.items():
            if status == "Low Risk":
                print(f"Patching Low Risk Vulnerability in Component {component}.")
                self.components[component] = "Safe"
            elif status == "High Risk":
                print(f"Component {component} requires premium service for High Risk Vulnerability.")
            else:
                print(f"Component {component} is already Safe.")

    def run(self):
        print("Initial System Status:")
        self.display_system()

        self.patch_system()

        print("\nFinal System Status:")
        self.display_system()

# Execute Task 4
task4 = SecurityAgent()
task4.run()
