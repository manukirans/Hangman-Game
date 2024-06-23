import random  # Import the random module to generate random numbers

from anime_data import anime_characters ,clue_anime_series

 
# Function to randomly select a character and return it along with its series as a cluer
def get_character():
    character = random.choice(anime_characters)
    clue = clue_anime_series.get(character, 'Anime')  # If character is not found in the clue dictionary, default to 'Anime'
    return character.upper(), clue

# Function to get the clue (anime series) for a given character
def get_clue(character):
    return clue_anime_series.get(character, 'Anime')  # If character is not found in the clue dictionary, default to 'Anime'

# Function to return the Hangman stages based on the number of attempts left
def hangman(attempt): 
 stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           - 
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           - 
        """,

        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,

        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,

        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
 return stages[attempt]

# Function to play the Hangman game

def play(character, clue_anime_series):
    
    hidden_character = "_" * len(character)  # Initialize the hidden character name with underscores
    
    guessed = False  # Flag to track if the character has been guessed
    
    guessed_letters = []  # List to store guessed letters
        
    guessed_words = []  # List to store guessed words
    
    attempt = 6  # Number of attempts allowed
    
    print(f"Welcome to the Anime Hangman Game!")
    print("Try to guess the character's name before running out of attempts.")
    print("Let's see how well you know your favorite anime characters!")
    print("")
    print(f"Your clue is: {clue_anime_series}")

    print(hangman(attempt))  # Print initial Hangman stage
    
    print(hidden_character)
    
    print("\n")
    
    # Main game loop
    while not guessed and attempt > 0:
        
        guess = input(f"Guess a letter or the complete name: ").upper()  # Accept user input and convert to uppercase
                
        if len(guess) == 1 and guess.isalpha():  # If guess is a single letter and is alphabetic
            
            if guess in guessed_letters:  # If letter has already been guessed
                
                print(f"You already guessed the letter - {guess} please try different")
                
            elif guess not in character:  # If letter is not in the character's name
                
                print(f"{guess} is not a letter in the name.")
                
                attempt -= 1  # Decrement attempts
                
                guessed_letters.append(guess)  # Add guessed letter to list
            else:
                print(f"Great, {guess} is in the name!")
                
                guessed_letters.append(guess)  # Add guessed letter to list
                
                # Update hidden character name to reveal guessed letters
                letter_list = list(hidden_character)
                
                indices = []
                                
                for i, letter in enumerate(character):
                    
                    if letter == guess:
                        
                        indices.append(i)
                        
                for index in indices:
                    
                    letter_list[index] = guess
                    
                hidden_character = "".join(letter_list)
                
                if "_" not in hidden_character:  # If there are no more underscores in hidden character name
                    
                    guessed = True  # Set guessed flag to True
                    
        elif len(guess) == len(character) and guess.isalpha():  # If guess is the complete name and is alphabetic
            
            if guess in guessed_words:  # If name has already been guessed
                
                print(f"You already guessed the name {guess}")
                
            elif guess != character:  # If guessed name is incorrect
                
                print(f"{guess} is not a valid name.")
                
                attempt -= 1  # Decrement attempts
                
                guessed_words.append(guess)  # Add guessed name to list
                
            else:
                guessed = True  # Set guessed flag to True
                
                hidden_character = character  # Reveal the complete character name
                
        else:
            print("Invalid guess.")  # If guess is not a valid letter or name
            
        print(hangman(attempt))  # Print Hangman stage corresponding to attempts left
        
        print(hidden_character)  # Print the hidden character name with revealed letters
        
        print("\n")
    # Game result
    if guessed:
        print(f"Congrats, you guessed the Character! You win!")
    else:
        print(f"Sorry, you ran out of attempts. The Character was {character}. Better luck next time!")

# Main function to start the game
def main():
    character, clue_anime_series = get_character()  # Get a random character and its clue
    
    play(character, clue_anime_series)  # Start the game with the selected character and clue
    
    # Loop to ask if the user wants to play again
    while input("Do you want to play again? (Y/N) ").upper() == "Y":
        
        character, clue_anime_series = get_character()  # Get a new random character and its clue
        
        play(character, clue_anime_series)  # Start the game again with the new character and clue

# Entry point of the program
if __name__ == "__main__":
    main()
