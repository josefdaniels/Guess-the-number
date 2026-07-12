# Guess The Number

A simple yet addictive command-line number guessing game written in Python.

---

## About

**Guess The Number** is a classic terminal game where the player must guess a randomly generated secret number within a limited number of attempts. The game features multiple difficulty levels, a scoring system, and bonus attempts for correct guesses.

## Features

- Clean and intuitive terminal interface
- Cross-platform screen clearing (Windows, Linux, macOS)
- Three difficulty levels with different ranges and starting attempts
- Persistent score across multiple rounds
- Bonus attempts on successful guesses
- Input validation and friendly error messages
- Simple navigation menu

## Requirements

- Python 3.6 or higher
- No external libraries required

## How to Run

1. Clone or download the project
2. Navigate to the project folder
3. Run the game:

```bash
python guessnumber.py
```
## How to Play
- Start the game from the main menu
- Choose your difficulty:
```
Easy — 5 attempts | Numbers 1 to 10
Medium — 3 attempts | Numbers 1 to 50
Hard — 1 attempt  | Numbers 1 to 100
```
- Enter your guesses when prompted
- After a correct guess you receive +1 point and +3 extra attempts
- The game continues until you run out of attempts

## Project Structure
```
Guess-the-number
├── README.md     
└── guessnumber.py
```
## Code Overview
- clear_screen(): Clears the terminal screen
- menu(): Displays main menu and returns user choice
- difficulty(): Handles difficulty selection and secret number generation
- Main game loop: Processes guesses, updates score and attempts

