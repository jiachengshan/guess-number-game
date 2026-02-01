import random


class WordGuessGame:
    def __init__(self, word_list, max_attempts=6):
        self.word_list = word_list
        self.max_attempts = max_attempts

        self.player_words = {
            "Player 1": random.choice(self.word_list),
            "Player 2": random.choice(self.word_list)
        }

        self.attempts_left = {
            "Player 1": max_attempts,
            "Player 2": max_attempts
        }

        self.current_player = "Player 1"
        self.other_player = "Player 2"
        self.game_over = False

    def switch_player(self):
        self.current_player, self.other_player = (
            self.other_player,
            self.current_player,
        )

    def check_guess(self, guess, secret_word):
        """
        Returns feedback string similar to Wordle:
        🟩 correct letter & position
        🟨 correct letter wrong position
        ⬜ not in word
        """
        feedback = []
        for i in range(len(guess)):
            if guess[i] == secret_word[i]:
                feedback.append("🟩")
            elif guess[i] in secret_word:
                feedback.append("🟨")
            else:
                feedback.append("⬜")
        return "".join(feedback)

    def make_guess(self, guess):
        secret_word = self.player_words[self.other_player]
        self.attempts_left[self.current_player] -= 1

        if guess == secret_word:
            self.game_over = True
            return "win", f"🎉 {self.current_player} guessed the word correctly!"

        feedback = self.check_guess(guess, secret_word)

        if self.attempts_left[self.current_player] == 0:
            self.game_over = True
            return "lose", (
                f"💀 {self.current_player} ran out of attempts.\n"
                f"{self.other_player}'s word was: {secret_word}"
            )

        self.switch_player()
        return "continue", feedback
