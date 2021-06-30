sec_word = "Omar"
user_guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while user_guess != sec_word and not(out_of_guesses):
    if guess_count < guess_limit:
        user_guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You've been defeated!")
else:
    print("You've conquered the world")