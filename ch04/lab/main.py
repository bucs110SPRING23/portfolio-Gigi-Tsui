import pygame
import random
import math

#part A
pygame.init()
pygame.event.get()
screen = pygame.display.set_mode((700, 700))

screen.fill("white")
center = 700/2
pygame.draw.circle(screen, "black", (center, center), 700/2)
pygame.draw.circle(screen, "red", (center, center), 340)

pygame.display.flip()
pygame.time.wait(1000)



#part B
import random

# distance_from_center = math.hypot (x1-x2, y1-y2) #the distance formula
# is_in_circle = distance_from_center <= width/2 #screen width
#loop that throws 10 random dartw in the board

for i in range (10):
    dart_y = random.randrange(0, 700)
    dart_x = random.randrange(0, 700)
    distance_from_center = math.hypot(center-dart_x, center-dart_y) #the distance formula
    # is_in_circle = distance_from_center <= width/2 #screen width
    if distance_from_center <= 340:
        is_in_circle = True
        pygame.draw.circle(screen, "green", (dart_x, dart_y), 10)
    else:
        is_in_circle = False
        pygame.draw.circle(screen, "black", (dart_x, dart_y), 10)

    pygame.display.flip()
    pygame.time.wait(1000)

pygame.display.quit()

