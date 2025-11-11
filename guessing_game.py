import random

levels = ["easy", "medium", "hard"]
ranges = [(1, 50, 15), (1, 100, 10), (1, 200, 7)]
highest_score = {level: None for level in levels}


def get_difficulty_level():

    print("Select Difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)\n")

    while True:
        user_choice = input("Your choice (1 to 3): ")
        if user_choice in ["1", "2", "3"]:
            return int(user_choice)
        else:
            print("Invalid choice! Please enter 1, 2, or 3")


def play_game():

    difficulty = get_difficulty_level()
    min_num, max_num, max_attempts = ranges[difficulty - 1]
    level = levels[difficulty - 1]
    target = random.randint(min_num, max_num)

    print(f"I'm thinking of a number between {min_num} and {max_num}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    for attempt in range(1, max_attempts + 1):

        print(
            f"Attempt {attempt} of {max_attempts} | Remaining: {max_attempts - attempt}"
        )
        user_guess = get_guess(min_num, max_num)

        if user_guess < target:
            print("📈 Too low! Try again.\n")
        elif user_guess > target:
            print("📉 Too high! Try again.\n")
        else:
            score = (max_attempts - attempt) * 10
            print("=" * 50)
            print("🎉 Congratulations! You won!")
            print(f"You guessed the number {user_guess} in {attempt} attempts!")
            print(f"Your score: {score} points")
            if update_highest_score(level, score):
                print(f"🏆 NEW BEST SCORE for difficulty level {level.title()}!")
            break
    else:
        print(f"😞 Game Over! You've used all {max_attempts} attempts.")
        print(f"The number was: {target}")
        print("Better luck next time!")
    print("=" * 50)


def get_guess(min_num, max_num):
    """Ask user for a number within a range and validate input"""
    while True:
        try:
            user_guess = int(input(f"Enter your guess ({min_num}-{max_num}): "))
            if min_num <= user_guess <= max_num:
                return user_guess
            print(f"Please enter a number between {min_num} and {max_num}!")
        except ValueError:
            print("Invalid input! Please enter a number.")


def update_highest_score(difficulty_level, score):

    current_highest_score = highest_score.get(difficulty_level)
    if current_highest_score is None or score > current_highest_score:
        highest_score[difficulty_level] = score
        return True
    return False


def show_statistics():

    print("\n=== BEST SCORES ===")
    for level in levels:
        print(f"{level.title()}: {highest_score[level] or 'Not played yet'}")


def main():
    """Main program"""
    print("🎮 WELCOME TO NUMBER GUESSING GAME 🎮\n")

    while True:
        print("=== New Game Started ===")
        play_game()
        show_statistics()

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("\nThanks for playing! Goodbye! 👋")
            break


main()
