# Uzd_04, 2021.01.15
# Spēle "Hangman" jeb "Karātavas" -uzmini vārdu pa burtam

from random import randint

print("Welcome to Hangman game!")

words = ["helicopter", "bus", "caterpillar"]  # Predefined words to guess
# failCount = 6

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
            print("Guessed letters: ", guessed)
            win = True  # True unless "-" drawed
            # draw guessing progress
            # print("Your word: ", "-"*len(word))  # general, to be changed to actual!
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

    else:
        print("Wrong choice! You entered: ", ans)
print("Exiting game... Bye!")
