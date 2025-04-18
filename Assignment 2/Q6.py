import random

class IntrusionDetectionGame:
    def __init__(self):
        self.actions_defender = ["Deploy Firewall", "Patch System", "Ignore Alerts"]
        self.actions_attacker = ["Brute Force Attack", "Phishing Attack", "Zero-Day Exploit", "Fake Attack", "Real Attack"]
        self.probability_zero_day = 0.5
        self.outcome_real_attack = 1
        self.outcome_fake_attack = 0

    def zero_day_exploit_outcome(self):
        return 1 if random.random() < self.probability_zero_day else 0

    def attacker_outcome(self, attacker_action):
        if attacker_action == "Brute Force Attack":
            return 0
        elif attacker_action == "Phishing Attack":
            return 1
        elif attacker_action == "Zero-Day Exploit":
            return self.zero_day_exploit_outcome()
        elif attacker_action == "Fake Attack":
            return 0
        elif attacker_action == "Real Attack":
            return self.outcome_real_attack
        return 0

    def minimax(self, depth, is_max_turn, game_state):
        if depth == 0:
            return game_state
        if is_max_turn:
            best_value = float('-inf')
            for action in self.actions_defender:
                game_state_new = game_state.copy()
                game_state_new[action] = 0
                best_value = max(best_value, self.minimax(depth - 1, False, game_state_new))
            return best_value
        else:
            best_value = float('inf')
            for action in self.actions_attacker:
                attacker_outcome = self.attacker_outcome(action)
                game_state_new = game_state.copy()
                game_state_new[action] = attacker_outcome
                best_value = min(best_value, self.minimax(depth - 1, True, game_state_new))
            return best_value

    def alpha_beta(self, depth, alpha, beta, is_max_turn, game_state):
        if depth == 0:
            return game_state
        if is_max_turn:
            best_value = float('-inf')
            for action in self.actions_defender:
                game_state_new = game_state.copy()
                game_state_new[action] = 0
                best_value = max(best_value, self.alpha_beta(depth - 1, alpha, beta, False, game_state_new))
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            return best_value
        else:
            best_value = float('inf')
            for action in self.actions_attacker:
                attacker_outcome = self.attacker_outcome(action)
                game_state_new = game_state.copy()
                game_state_new[action] = attacker_outcome
                best_value = min(best_value, self.alpha_beta(depth - 1, alpha, beta, True, game_state_new))
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_value

    def expected_value(self, action):
        if action == "Zero-Day Exploit":
            return self.probability_zero_day * 1 + (1 - self.probability_zero_day) * 0
        return 0

game = IntrusionDetectionGame()
game_state = {}
game_state["Deploy Firewall"] = 0
game_state["Patch System"] = 0
game_state["Ignore Alerts"] = 0

def minimax_decision():
    return game.minimax(3, True, game_state)

def alpha_beta_decision():
    return game.alpha_beta(3, float('-inf'), float('inf'), True, game_state)

def expected_value_decision():
    return game.expected_value("Zero-Day Exploit")

print("Minimax decision value:", minimax_decision())
print("Alpha-beta decision value:", alpha_beta_decision())
print("Expected value of Zero-Day Exploit:", expected_value_decision())
