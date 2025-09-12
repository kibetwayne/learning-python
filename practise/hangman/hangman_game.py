import random
from hangman_art import logo, stages
from hangman_words import words

print(logo)

choosen = random.choice(words)
word_len = len(choosen)
lives = 6

#creating a blank list
blank = []
blank = ["_"] * len(choosen)

end_of_game = False
while not end_of_game and lives >0:    
    guess = input('what is your letter: ').lower()
    
    #check if the letter is already guessed
    if guess in blank:
        print(f'you have already guessed {guess}')

    #check guessed letter
    for i in range(word_len):
        if guess == choosen[i]:
                blank[i] = guess
    print(" ".join(blank))

    #check if user's guess is wrong
    if guess not in choosen:
        print(f'{guess} is not in the word you lose a life')
        lives -= 1
        print(f'you have {lives} lives left')

    print(stages[lives])

    #check if user has got all letters
    if '_' not in blank:
        end_of_game = True
        print('you win')

#check if user has run out of lives    
if lives == 0:
    print('you lose')
    print(f'the word is {choosen}')



