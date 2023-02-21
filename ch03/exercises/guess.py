import random
import pygame
print(random.randint(1,10))

user_guess = input("Guess a number between 1 and 10")
guess = int(user_guess)





    print("You Entered:", user_guess)
    print("The correct patter was", colors)

    if user_guess == colors:
        print("Correct! You win.")
    else:
        print("Were you even paying attention?")

    pygame.quit()



    pygame.init()
screen = pygame.display.set_mode()