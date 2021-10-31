# brings in a random word
import random
word_list = open("words.txt").read().split()
easy_word = []
medium_word = []
hard_word = []
        

input("Please select easy, medium, or hard ")
difficulty = input()
# 4-6 characters
if difficulty == "easy":
    for word in word_list:
        if len(word) >= 4 and len(word) <= 6:
            easy_word.append(word)

word = (random.choice(easy_word))
            

# if difficulty == "medium":
#     print(difficulty)
# if difficulty == "hard":
#     print(difficulty)

# word = "butter"

tries = 8
display = "_" *len(word)
game_over = False

while not game_over:
    print("You have " + str(tries) + " remaining")
    print(display)
    guess = input("Please guess a letter ")

    i = 0
    if guess in word:
        while word.find(guess, i) != -1:
            i = word.find(guess, i)
            display = display[:i] + guess + display[i +1:]
            i += 1
        print("Correct")
    else:
        print("Sorry, Wrong Guess")
        tries -= 1

    if word == display:
        print("You Win")
        print("Would you like to play again?")
        game_over = True

    if tries == 0:
        print("Sorry, you are out of tries.")
        game_over = True