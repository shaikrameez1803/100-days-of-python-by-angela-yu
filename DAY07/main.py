import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ""
for _ in range(word_length):
    display += "_"

print("Word to guess: " + display)

game_over = False
guessed_letters = []

while not game_over:

    print(f"****************************/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        continue
    guessed_letters.append(guess)

    new_display = ""

    for i in range(word_length):
        if chosen_word[i] == guess:
            new_display += guess
        else:
            new_display += display[i]

    display = new_display
    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print("***********************YOU LOSE***********************")
            print(f"******** IT WAS {chosen_word}! ********")

    if "_" not in display:
        game_over = True
        print("***********************YOU WIN***********************")

    print(stages[lives])
