import random
from hangman_words import wordListEasy, wordListMedium, wordListDifficult, wordListVeryDifficult
from hangman_art import stages, logo

print(logo)

difficultyLevel = input("What difficulty level do you want to play?\n1 for easy, 2 for medium, 3 for difficult or 4 for very difficult\n")
if difficultyLevel == "1":
    word = random.choice(wordListEasy)
elif difficultyLevel == "2":
    word = random.choice(wordListMedium)
elif difficultyLevel == "3":
    word = random.choice(wordListDifficult)
elif difficultyLevel == "4":
    word = random.choice(wordListVeryDifficult)
print(word)

wordLength = len(word)
placeHolder = "_ " * wordLength
print(placeHolder)


lives = 7
gameOver = False
correctLetters = []
incorrectLetters = []
hintLetters = []

while not gameOver:
    print(f"****************************{lives}/7 LIVES LEFT****************************")
    display = ""

    hint = random.choice(word)

    if lives < 4:
        hintQ = input("Do you want a hint? ").lower()
        if hintQ == "yes":
            hintLetters.append(hint)
            print(f"Hint: {hint} is in the word")
            for char in word:
                if char == hint:
                    display += char


    letter = input("Guess a letter: ").lower()
    
    if letter in correctLetters:
        print(f"You have already guessed {letter}")
    if letter in hintLetters:
        print(f"{letter} has already been revealed")


    for char in word:
        if char == letter:
            display += char
            correctLetters.append(letter)
        elif char in correctLetters:
            display += char
        else:
            display += "_ "
       

    if letter not in word:
        if letter in incorrectLetters:
            print(f"You have already guessed {letter}, it is not in the word")

        else:
            lives -= 1
            incorrectLetters.append(letter)
            print(f"{letter} is not in the word,\ntry again")

        if lives == 0:
            gameOver = True
            print(f"***********************The correct word was {word}\nYOU LOSE**********************")

    print(display)
    print(stages[lives])
    
    if "_ " not in display:
        gameOver = True
        print("****************************YOU WIN****************************")
    
