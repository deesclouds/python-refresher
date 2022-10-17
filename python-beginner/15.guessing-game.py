# Guessing Game

secret_word = 'giraffe'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    #check to see if they haven't used all their guesses
    if guess_count < guess_limit:
        guess = input('Enter guess: ')
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("No more guesses, You Lost.")
else:
    print("You win!\nYou've guessed the correct secret word!")

