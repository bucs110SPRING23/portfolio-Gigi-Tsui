import random
import pygame
correct_answer = print(random.randint(1,10))

user_guess = input("Guess a number between 1 and 10")
guess = int(user_guess)


guess = ""
if guess == user_guess:
    print ("Correct! You Win.")
    pygame.quit()
elif guess < user_guess:
    print ("the number is higher,")
else:
    print("The number is lower")

limit = 3
for i in range(limit):
    if (i == limit - 1, limit == 0):
        print ("game over")


pygame.quit()
