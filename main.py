from game import WordGuessGame


def load_words():
    # 可以随便加词，老师会很喜欢这个“可扩展”
    return [
        "apple", "grape", "peach", "lemon", "mango",
        "berry", "melon", "cherry", "olive", "plums"
    ]


def main():
    print("🎮 Welcome to WORD DUEL!")
    print("Two players take turns guessing each other's secret word.")
    print("🟩 correct letter & position | 🟨 correct letter | ⬜ not in word\n")

    words = load_words()
    game = WordGuessGame(words)

    while not game.game_over:
        player = game.current_player
        attempts = game.attempts_left[player]

        print(f"\n🔁 {player}'s turn | Attempts left: {attempts}")
        guess = input("Enter a 5-letter word: ").lower().strip()

        if len(guess) != 5 or not guess.isalpha():
            print("❌ Invalid input. Please enter a 5-letter word.")
            continue

        status, message = game.make_guess(guess)
        print(message)

    print("\n🏁 Game Over. Thanks for playing!")


if __name__ == "__main__":
    main()
