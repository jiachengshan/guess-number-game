import random


class WordGuessGame:
    def __init__(self, words, word_length, max_attempts):
        self.word_length = word_length
        self.max_attempts = max_attempts

        self.player_words = {
            "Player 1": random.choice(words),
            "Player 2": random.choice(words)
        }

        self.attempts_left = {
            "Player 1": max_attempts,
            "Player 2": max_attempts
        }

        self.scores = {
            "Player 1": 0,
            "Player 2": 0
        }

        self.current_player = "Player 1"
        self.other_player = "Player 2"
        self.game_over = False
        self.winner = None

    def switch_player(self):
        self.current_player, self.other_player = (
            self.other_player,
            self.current_player
        )

    def check_guess(self, guess, secret_word):
        feedback = []
        for i in range(len(guess)):
            if guess[i] == secret_word[i]:
                feedback.append("🟩")
            elif guess[i] in secret_word:
                feedback.append("🟨")
            else:
                feedback.append("⬜")
        return "".join(feedback)

    def calculate_score(self, attempts_left):
        return attempts_left * 10

    def make_guess(self, guess):
        secret_word = self.player_words[self.other_player]
        self.attempts_left[self.current_player] -= 1

        # Correct guess
        if guess == secret_word:
            self.game_over = True
            self.winner = self.current_player
            self.scores[self.current_player] += self.calculate_score(
                self.attempts_left[self.current_player]
            )
            return "win", f"🎉 {self.current_player} guessed the word!"

        feedback = self.check_guess(guess, secret_word)

        # Out of attempts
        if self.attempts_left[self.current_player] == 0:
            self.game_over = True
            self.winner = self.other_player
            return "lose", (
                f"💀 {self.current_player} ran out of attempts.\n"
                f"The word was: {secret_word}"
            )

        self.switch_player()
        return "continue", feedback
