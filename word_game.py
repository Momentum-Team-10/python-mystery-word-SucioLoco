input("Please select easy, medium, or hard ")
difficulty = input()
if difficulty == "easy":
    print(difficulty + "easy")
if difficulty == "medium":
    print(difficulty)
if difficulty == "hard":
    print(difficulty)

# word = "butter"

# tries = 8
# display = "_" *len(word)
# game_over = False

# while not game_over:
#     print("You have " + str(tries) + " remaining")
#     print(display)
#     guess = input("Please guess a letter ")

#     i = 0
#     if guess in word:
#         while word.find(guess, i) != -1:
#             i = word.find(guess, i)
#             display = display[:i] + guess + display[i +1:]
#             i += 1
#         print("Correct")
#     else:
#         print("Sorry, Wrong Guess")
#         tries -= 1

#     if word == display:
#         print("You Win")
#         print("Would you like to play again?")
#         game_over = True

#     if tries == 0:
#         print("Sorry, you are out of tries.")
#         game_over = True