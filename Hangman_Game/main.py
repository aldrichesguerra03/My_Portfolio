import random
from hangman_logo import stages, logo

from hangman_words import movie_list, food_list, song_list

#Boolean
end_of_game = False

#Number of Lives
lives = 6
available_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y,', 'z'

                     ]
print("""
1. movies
2. songs
3. foods
""")
choose_category = int(input("type the number of your desired category: "))
if choose_category == 1:
    chosen_word = movie_list
elif choose_category == 2:
    chosen_word = song_list
elif choose_category == 3:
    chosen_word = food_list

random_word = random.choice(chosen_word)
word_length = len(random_word)


#Testing code
#print(f'Pssst, the solution is {random_word}.')
print(logo)
#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess not in available_letters:
        print(f"You've already guessed letter {guess}.")
    elif guess in available_letters:
        available_letters.remove(guess)




    #Check guessed letter
    for position in range(word_length):
        letter = random_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            print(stages[lives])


    if guess not in list(random_word):
        lives -= 1
        print(stages[lives])
        print(f"Letter {guess} is not in the word.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")



