import random


class GuessNumberGame:
    def __init__(self, max_number=100, max_attempts=7):
        self.max_number = max_number
        self.max_attempts = max_attempts
        self.secret_number = random.randint(1, self.max_number)
        self.attempts = 0
        self.is_over = False

    def make_guess(self, guess):
        self.attempts += 1

        if guess == self.secret_number:
            self.is_over = True
            return "correct"
        elif guess < self.secret_number:
            return "too low"
        else:
            return "too high"

    def has_attempts_left(self):
        return self.attempts < self.max_attempts
