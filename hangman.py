from random import randint # Do not delete this line
word = ""


def displayIntro():
    with open("intro.txt", "r") as intro:
        print(intro.read())

def displayEnd(result):
    if (result):
        print("Hidden word was:  ", word)
        with open("end_won.txt", "r") as win:
            print(win.read())
    else:
        displayHangman(5)
        print("Hidden word was:  ", word)
        with open("end_lost.txt", "r") as lost:
            print(lost.read())


def displayHangman(state):  
    hangman = open("hangman_states.txt", "r").readlines()
    text = ""
    for i in range(state * 8, state * 8 + 8):
        text = text + hangman[i]
    
    print(text)

def getWord():
    with open("hangman-words.txt", "r") as words:
        words = words.read().splitlines()
        return words[randint(0, len(words) - 1)]

def valid(c):
    if (len(c) != 1):
        return False
    if (c.isalpha() & c.islower()):
        return True

    return False

def play():
    global word 
    word = getWord()
    guess = ["_"] * len(word)

    state = 0
    while True:
        displayHangman(state)
        print("\n\nGuess a letter: ", "".join(guess))
        
        c = input("\nEnter the letter: ")
        while (not valid(c)):
            c = input("Enter the letter: ")
        
        found = False
        if (c not in guess):
            for index in range(0, len(word)):
                if (word[index] == c):
                    found = True
                    guess[index] = c
        if (not found):
            state += 1

        if ("_" not in guess):
            result = True
            break
        elif (state == 5):
            result = False
            break

    return result

def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)

        print("\nDo you want to play again? (yes/no)")
        if (input().lower() != "yes"):
            return

if __name__ == "__main__":
    hangman()
