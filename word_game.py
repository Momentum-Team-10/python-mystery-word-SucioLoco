# brings in a random word
import random
word_list = open("words.txt").read().split()
word_selection = []
        

input("Please select easy, medium, or hard ")
difficulty = input()
# 4-6 characters
if difficulty == "easy":
    for word in word_list:
        if len(word) >= 4 and len(word) <= 6:
            word_selection.append(word)
elif difficulty == "medium":
    for word in word_list:
        if len(word) >= 6 and len(word) <= 8:
            word_selection.append(word)
elif difficulty == "hard":
    for word in word_list:
        if len(word) > 8:
            word_selection.append(word)
else: print("Please type in easy, medium, or hard")

print(random.choice(word_selection))
#     for word in word_list:
#         if len(word) >= 6 and len(word) <= 8:
#             medium_word.append(word)

# word = (random.choice(medium_word))
            

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
    guess = input("Please guess a letter ") [0]

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
        print("The word was " +word)