# 🎮 Hangman Game (Python)

A classic terminal-based Hangman game written in Python. This beginner-friendly project challenges the player to guess a hidden word one letter at a time — with only 6 lives before the stickman is "hanged"!

## 📌 Features

- Random word selection from a predefined list.
- Visual hangman stages drawn in ASCII art.
- Tracks guessed letters and prevents repeated guesses.
- Win or lose logic with clear end messages.
- Fully playable in a terminal or command prompt.

## 🧑‍💻 How to Play

1. Run the Python script in a terminal.
2. Guess one letter at a time.
3. You have 6 lives. Each wrong guess costs 1 life.
4. If you guess the word before running out of lives — you win!
5. If your lives reach 0 — the hangman is complete, and you lose.

## ▶️ Example Gameplay

🎮 Welcome to Hangman!

Lives remaining: 6
Guess a letter: o
✅ Good guess!

_ _ _ _ o _
Lives remaining: 6
Guess a letter: z
❌ Wrong guess!

+---+
| |
O |
|
|
|
Lives remaining: 5


## 📂 Word List

The game randomly selects from:

- python
- java
- kotlin
- javascript

You can expand this list in the `word_list` variable.

## 🛠 Requirements

- Python 3.x

No external libraries are needed.

## 🚀 Running the Game

```bash
python hangman.py
🙌 Credits
Made by Shafin as a fun Python project to learn loops, conditionals, and list handling.
