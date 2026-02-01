from game import WordGuessGame


def load_words(word_length):
    with open("words.txt", "r") as f:
        return [w.strip().lower() for w in f if len(w.strip()) == word_length]


def choose_difficulty():
    print("Choose difficulty:")
    print("1) Easy   (4 letters, 8 attempts)")
    print("2) Normal (5 letters, 6 attempts)")
    print("3) Hard   (6 letters, 5 attempts)")

    choice = input("Enter 1 / 2 / 3: ").strip()

    if choice == "1":
        return 4, 8
    elif choice == "3":
        return 6, 5
    else:
        return 5, 6


def main():
    print("🎮 Welcome to WORD DUEL!")
    print("Two players take turns guessing each other's secret word.")
    print("🟩 correct position | 🟨 correct letter | ⬜ not in word\n")

    word_length, max_attempts = choose_difficulty()
    words = load_words(word_length)

    game = WordGuessGame(words, word_length, max_attempts)

    while not game.game_over:
        player = game.current_player
        attempts = game.attempts_left[player]

        print(f"\n🔁 {player}'s turn | Attempts left: {attempts}")
        guess = input(f"Enter a {word_length}-letter word: ").lower().strip()

        if len(guess) != word_length or not guess.isalpha():
            print("❌ Invalid input.")
            continue

        status, message = game.make_guess(guess)
        print(message)

    print("\n🏁 Game Over!")
    print(f"🏆 Winner: {game.winner}")
    print("Final Scores:")
    for p, s in game.scores.items():
        print(f"{p}: {s}")


if __name__ == "__main__":
    main()
