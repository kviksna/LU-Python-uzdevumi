# Uzd_04, 2021.01.15
# Spēle "Hangman" jeb "Karātavas" -uzmini vārdu pa burtam

from random import randint

def draw_hang(faults):
    print(' +---+')
    print('  |   |')
    if faults >= 1:
        print('  O   |')
    else:
        print('      |')

    if faults >= 4:
        print(' /|\  |')
    elif faults >= 3:
        print(' /|   |')
    elif faults >= 2:
        print('  |   |')
    else:
        print('      |')

    if faults == 6:
        print(' / \  |')
    elif faults >= 5:
        print('   \  |')
    else:
        print('      |')
    print('      |')
    print('='*9)  # '========='

words = ["helicopter", "bus", "caterpillar"]  # Predefined words to guess

print("Welcome to Hangman game!")

while True:  # main menu
    print("")  # New line
    print(f"Words stored: {len(words)}")
    print("[1] to play Hangman")
    print("[2] to add new word")
    print("[3] to exit game")
    try:
        ans = int(input("Your choice: "))
    except ValueError:
        print("Wrong choice! You entered non integer value!")
        continue
    if ans == 3:
        break
    elif ans == 2:
        words.append(input("Add new word: ").lower())
    elif ans == 1:
        word = words[randint(0, len(words)-1)]
        lives = 6
        guessed = []  # guessed letters
        while lives:
            draw_hang(6-lives)  # convert to faults
            print("Guessed letters: ", end="")
            print(*guessed, sep=",")
            win = True  # True unless "-" drawed
            # draw guessing progress
            for i in word:
                if i in guessed:
                    print(i, end="")
                else:
                    win = False
                    print("-", end="")
            print("")  # EOL
            if win:
                print("You won!")
                break  # goto main menu
            guess = input("Guess letter: ").lower()
            guessed.append(guess)
            if guess not in word:
                lives -= 1
            if lives == 0:
                print(word)
                print("You lost!")
    else:
        print("Wrong choice! You entered: ", ans)
print("Exiting game... Bye!")
