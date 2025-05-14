import random

# Hangman visual stages
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Step 1: Welcome message and word selection
print("🎮 Welcome to Hangman!")
word_list = ["python", "java", "kotlin", "javascript"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Step 2: Game setup
lives = 6
display = ["_"] * word_length
guessed_letters = []

# Step 3: Main game loop
while True:
    print("\n" + " ".join(display))
    print(f"Lives remaining: {lives}")
    
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("❗ You've already guessed that letter. Try a different one.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in chosen_word:
        for index in range(word_length):
            if chosen_word[index] == guess:
                display[index] = guess
        print("✅ Good guess!")

    # Wrong guess
    else:
        lives -= 1
        print("❌ Wrong guess!")
        print(stages[6 - lives])  # Show hangman stage based on lives lost

    # Check win condition
    if "_" not in display:
        print("\n🎉 You win! The word was:", chosen_word)
        break

    # Check lose condition
    if lives == 0:
        print("\n💀 You lost! The word was:", chosen_word)
        break
