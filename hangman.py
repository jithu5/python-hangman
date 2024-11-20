from words import words
import random
import string

def random_word_validater():
    # Generate a random word from the list of English words
    random_word = random.choice(words).upper()
    # Check if the word contains any special characters or spaces
    while  any(char in random_word for char in "-_ "):
        random_word = random.choice(words).upper()

    return random_word

random_word = random_word_validater()
alphabets = set(string.ascii_uppercase)
guessed_letter = set()
attempts = 10

print("\nWelcome to Hangman!")
print(f"The word has {len(random_word)} letters.")

def play_game():
    # Initialize the number of attempts to 10
    global attempts
    # Start the game loop until the user has won or run out of attempts
    while attempts >0 :
        print('*'*50)
        # Display the word with guessed letters and dashes for unguessed ones
        word_list = [letter if letter in guessed_letter else '_' for letter in random_word]
        print("\nCurrent word: ", ' '.join(word_list))
        print(f"Guessed letters: {', '.join(sorted(guessed_letter)) if guessed_letter else 'None'}")

        # Check if the user has won
        if '_' not in word_list:
                print('Congratulations, you have guessed the word correctly!')
                break

        print(f"You have {attempts} attemts to guess...")
        user_guessed = input('Enter the letter you have guessed: ').upper()

        # Validate the input
        if len(user_guessed) != 1 :
            print("Invalid input. Please enter a single letter.")
            continue
        print('*'*50)
        # chack if the letter is present or not
        if user_guessed in alphabets - guessed_letter:
            guessed_letter.add(user_guessed)
            if user_guessed in random_word:
                print(f'Congratulations, {user_guessed} is a correct letter.')
                continue
            else:
                print(f'Sorry, {user_guessed} is not a correct letter.')
                attempts = attempts - 1
        elif user_guessed in guessed_letter:
            print('You have already guessed that letter.')
        else:
            print('Invalid input. Please enter a letter.')
            continue
        
    # End the game if the player runs out of attempts
    if attempts == 0:
        print(f"\nGame over! The word was: {random_word}")
        print("Better luck next time!")

play_game()