from game import GuessNumberGame


def main():
    print("🎮 Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 attempts.\n")

    game = GuessNumberGame()

    while not game.is_over and game.has_attempts_left():
        user_input = input("Enter your guess: ")

        if not user_input.isdigit():
            print("❌ Please enter a valid number.\n")
            continue

        guess = int(user_input)
        result = game.make_guess(guess)

        if result == "correct":
            print(f"🎉 You win! The number was {game.secret_number}.")
        else:
            print(f"➡️ Your guess is {result}.")
            print(f"Attempts left: {game.max_attempts - game.attempts}\n")

    if not game.is_over:
        print(f"💀 Game over! The number was {game.secret_number}.")


if __name__ == "__main__":
    main()
