import random

anime_characters = [
    'Luffy', 'Zoro', 'Nami', 'Sanji', 'Usopp', 'Chopper', 'Robin', 'Franky', 'Brook', 'Jinbe',  # One Piece
    'Ichigo', 'Rukia', 'Renji', 'Orihime', 'Uryu', 'Byakuya', 'Kenpachi', 'Toshiro', 'Gin', 'Aizen',  # Bleach
    'Gojo', 'Yuji', 'Megumi', 'Nobara', 'Sukuna', 'Maki', 'Panda', 'Yuta', 'Kugisaki', 'Inumaki',  # Jujutsu Kaisen
    'Goku', 'Vegeta', 'Gohan', 'Piccolo', 'Frieza', 'Cell', 'MajinBuu', 'Trunks', 'Krillin', 'Bulma',  # Dragon Ball Z
    'Tanjiro', 'Nezuko', 'Zenitsu', 'Inosuke', 'Giyu', 'Shinobu', 'Kanao', 'Tengen', 'Muzan', 'Rengoku',  # Demon Slayer
    'Asta', 'Yuno', 'Noelle', 'Yami', 'Magna', 'Luck', 'Fuegoleon', 'Vetto', 'Vanessa', 'William',  # Black Clover
    'SungJinWoo', 'ChaHaeIn', 'Igris', 'Beru', 'YooJinHo', 'GoGunHee', 'BaeYoonSik', 'LeeJuHee', 'SongJiHoon', 'KangTaeShik'  # Solo Leveling
]

clue_anime_series = {
    'Luffy': 'One Piece',
    'Zoro': 'One Piece',
    'Nami': 'One Piece',
    'Sanji': 'One Piece',
    'Usopp': 'One Piece',
    'Chopper': 'One Piece',
    'Robin': 'One Piece',
    'Franky': 'One Piece',
    'Brook': 'One Piece',
    'Jinbe': 'One Piece',
    'Ichigo': 'Bleach',
    'Rukia': 'Bleach',
    'Renji': 'Bleach',
    'Orihime': 'Bleach',
    'Uryu': 'Bleach',
    'Byakuya': 'Bleach',
    'Kenpachi': 'Bleach',
    'Toshiro': 'Bleach',
    'Gin': 'Bleach',
    'Aizen': 'Bleach',
    'Gojo': 'Jujutsu Kaisen',
    'Yuji': 'Jujutsu Kaisen',
    'Megumi': 'Jujutsu Kaisen',
    'Nobara': 'Jujutsu Kaisen',
    'Sukuna': 'Jujutsu Kaisen',
    'Maki': 'Jujutsu Kaisen',
    'Panda': 'Jujutsu Kaisen',
    'Yuta': 'Jujutsu Kaisen',
    'Kugisaki': 'Jujutsu Kaisen',
    'Inumaki': 'Jujutsu Kaisen',
    'Goku': 'Dragon Ball Z',
    'Vegeta': 'Dragon Ball Z',
    'Gohan': 'Dragon Ball Z',
    'Piccolo': 'Dragon Ball Z',
    'Frieza': 'Dragon Ball Z',
    'Cell': 'Dragon Ball Z',
    'MajinBuu': 'Dragon Ball Z',
    'Trunks': 'Dragon Ball Z',
    'Krillin': 'Dragon Ball Z',
    'Bulma': 'Dragon Ball Z',
    'Tanjiro': 'Demon Slayer',
    'Nezuko': 'Demon Slayer',
    'Zenitsu': 'Demon Slayer',
    'Inosuke': 'Demon Slayer',
    'Giyu': 'Demon Slayer',
    'Shinobu': 'Demon Slayer',
    'Kanao': 'Demon Slayer',
    'Tengen': 'Demon Slayer',
    'Muzan': 'Demon Slayer',
    'Rengoku': 'Demon Slayer',
    'Asta': 'Black Clover',
    'Yuno': 'Black Clover',
    'Noelle': 'Black Clover',
    'Yami': 'Black Clover',
    'Magna': 'Black Clover',
    'Luck': 'Black Clover',
    'Fuegoleon': 'Black Clover',
    'Vetto': 'Black Clover',
    'Vanessa': 'Black Clover',
    'William': 'Black Clover',
    'SungJinWoo': 'Solo Leveling',
    'ChaHaeIn': 'Solo Leveling',
    'Igris': 'Solo Leveling',
    'Beru': 'Solo Leveling',
    'YooJinHo': 'Solo Leveling',
    'GoGunHee': 'Solo Leveling',
    'BaeYoonSik': 'Solo Leveling',
    'LeeJuHee': 'Solo Leveling',
    'SongJiHoon': 'Solo Leveling',
    'KangTaeShik': 'Solo Leveling'
}

def get_character():
    character = random.choice(anime_characters)
    clue = clue_anime_series.get(character,'Anime')
    return character.upper() , clue

def get_clue(character):
    return clue_anime_series.get(character,'Anime')

def hangman(attempt):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           - "You killed him"
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

def play(character, clue_anime_series):
    hidden_character = "_" * len(character)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempt = 6
    print(f"Welcome to the Anime Hangman Game!")
    print("Try to guess the character's name before running out of attempts.")
    print("Let's see how well you know your favorite anime characters!")
    print("")
    print(f"Your clue is: {clue_anime_series}")

    print(hangman(attempt))
    print(hidden_character)
    print("\n")
    while not guessed and attempt > 0:
        guess = input(f"Guess a letter or the complete name: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter - {guess}")
            elif guess not in character:
                print(f"{guess} is not a letter in the name.")
                attempt -= 1
                guessed_letters.append(guess)
            else:
                print(f"Great, {guess} is in the name!")
                guessed_letters.append(guess)
                letter_list = list(hidden_character)
                indices = []
                for i, letter in enumerate(character):
                    if letter == guess:
                        indices.append(i)

                for index in indices:
                    letter_list[index] = guess
                hidden_character = "".join(letter_list)
                if "_" not in hidden_character:
                    guessed = True
        elif len(guess) == len(character) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the name {guess}")
            elif guess != character:
                print(f"{guess} is not a valid name.")
                attempt -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                hidden_character = character
        else:
            print("Invalid guess.")
        print(hangman(attempt))
        print(hidden_character)
        print("\n")
    if guessed:
        print(f"Congrats, you guessed the Character! You win!")
    else:
        print(f"Sorry, you ran out of attempts. The Character was {character}. Better luck next time!")

def main():
    character, clue_anime_series = get_character()
    play(character, clue_anime_series)
    while input("Do you want to play again? (Y/N) ").upper() == "Y":
        character, clue_anime_series = get_character()
        play(character, clue_anime_series)

if __name__ == "__main__":
    main()
