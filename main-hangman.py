#create a wordlist
import random
from hangman_words import word_list
choosen_word = random.choice(word_list)
#give hint of word length
word_len = len(choosen_word)
end_of_game = False
lives = 6

from hangman_art import logo
print(logo)
#testing code
print(f'the word is {choosen_word}')
display = []

for letter in range(word_len):
    display += "_"
print(display)


while not end_of_game:
#take input from user
    guess = input("Guess a letter:").lower()
    #print the corect gussed letter in the blank 

    if guess in display:
       print(f"You've already guessed{guess}")
    
    for position in range(word_len):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in choosen_word:
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You loose")
    print(f"{' '.join(display)}")    

    if "_" not in display:
        end_of_game = True
        print("You win ")

    from hangman_art import stages
    print(stages[lives])