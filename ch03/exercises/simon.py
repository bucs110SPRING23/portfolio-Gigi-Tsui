## Events: when a user interacts with a window 
# operating systems handles events which is basically  
#your program ->operating system: anything happening?

##OD => event
##type of event == operating
# - clicking
# - key_presses

#connect actions to algorthms

#lets build a game of simon says

import pygame
import random
pygame.init()
screen = pygame.display.set_mode()
colors = ["red", "blue", "yellow", "green"]
random.shuffle(colors)


for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(250)


message = ''
Simon says:
    UP: RED
    DOWN: BLUE
    LEFT: GREEN
    RIGHT:YELLOW

    #Click on the window, enter sequence, m then press enter in the console


response = input(message)

#pygame.EVENT_OBJECT


user_guess = []
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            print("UP")
            user_guess.append("red")
        elif event.key == pygame.K_DOWN:
            print("DOWN")
            user_guess.append("blue")
        elif event.key == pygame.K_LEFT:
            print("LEFT")
            user_guess.append("green")
        elif event.key == pygame.K_RIGHT:
            print(RIGHT)
            user_guess.append("yellow")
    


        pygame.display.flip()
        pygame.time.wait(1000)

    print("You Entered:", user_guess)
    print("The correct pattern was", colors)

    if user_guess == colors:
        print("Correct! You win.")
    else:
        print("Were you even paying attention?")

    pygame.quit()