# Number Guessing Game

A simple Python-based number guessing game demonstrating core programming concepts, including input handling, control flow, functions, loops, error handling, and basic data structures.

## Features

- Three difficulty levels:
  - Easy (1–50, 15 attempts)
  - Medium (1–100, 10 attempts)
  - Hard (1–200, 7 attempts)
- Random number generation
- Higher/Lower hints for each guess
- Score calculation based on remaining attempts
- Best score tracking per difficulty level
- Replay option
- Input validation

## Learning Objectives

* Use of functions and modular code structure
* Handling user input with validation
* Loops and conditional logic
* Working with lists, tuples, and dictionaries
* Basic error handling with `try/except`

## 🕹️ Example Gameplay

🎮 WELCOME TO NUMBER GUESSING GAME 🎮

=== New Game Started ===
Select Difficulty:      
1. Easy (1-50)
2. Medium (1-100)       
3. Hard (1-200)

Your choice (1 to 3): 1 
I'm thinking of a number between 1 and 50.
You have 15 attempts. Good luck!

Attempt 1 of 15 | Remaining: 14
Enter your guess (1-50): 25
📉 Too high! Try again.        

Attempt 2 of 15 | Remaining: 13
Enter your guess (1-50): 15    
📉 Too high! Try again.        

Attempt 3 of 15 | Remaining: 12
Enter your guess (1-50): 7     
📉 Too high! Try again.        

Attempt 4 of 15 | Remaining: 11
Enter your guess (1-50): 5     
📉 Too high! Try again.        

Attempt 5 of 15 | Remaining: 10
Enter your guess (1-50): 3     
📉 Too high! Try again.

Attempt 6 of 15 | Remaining: 9
Enter your guess (1-50): 1
==================================================
🎉 Congratulations! You won!
You guessed the number 1 in 6 attempts!
Your score: 90 points
🏆 NEW BEST SCORE for difficulty level Easy!
==================================================

=== BEST SCORES ===
Easy: 90
Medium: Not played yet
Hard: Not played yet

Do you want to play again? (yes/no): no

Thanks for playing! Goodbye! 👋
