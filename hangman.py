word_list = ["superman" , "butter" , "computer" , "bucket" , "starbucks" , "pizza" , "anaconda" , "engineer"]
import random
hangman = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
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
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_" 
print(placeholder)

correct_letters = []

game_over = False   

while not game_over:
    guess = input("Guess any letter : ").lower()
     
    display = ""
    for letter in chosen_word:
         if (guess == letter):
           display += letter
           correct_letters.append(guess)
         elif letter in correct_letters:
             display += letter
         else:
           display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("YOU LOOSE!")

    if "_" not in display:
        game_over = True
        print("YOU WIN!")


    print(hangman[lives])

