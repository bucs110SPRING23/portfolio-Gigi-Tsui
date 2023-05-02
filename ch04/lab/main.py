import pygame
import random
import math

#part A
pygame.init()
pygame.event.get()
screen = pygame.display.set_mode((700, 700))

hit_box_width = 200
hit_box_height = 200

hitboxes = {
    "red": pygame.Rect(100, 200, hit_box_width, hit_box_height),
    "blue": pygame.Rect(400, 200, hit_box_width, hit_box_height),
}

center = 700/2
p1_score = 0
p2_score = 0
bet = True
darts = False
guess = ""
font = pygame.font.Font(None, 48)

while bet == True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hitboxes["red"].collidepoint(event.pos):
                guess = "red"
                bet = False
                darts = True
            elif hitboxes["blue"].collidepoint(event.pos):
                guess = "blue"
                bet = False
                darts = True

    screen.fill("white")
    text = font.render("choose who to bet on", True, "black")
    screen.blit(text, (100, 100)) # where <x> and<y> are coordinates on screen
    pygame.draw.rect(screen, "red", hitboxes["red"])
    pygame.draw.rect(screen, "blue", hitboxes["blue"])
    pygame.display.flip()


while darts == True:
    screen.fill("white")
    pygame.draw.circle(screen, "black", (center, center), 700/2)
    pygame.draw.circle(screen, "green", (center, center), 340)

    for i in range (10):
        print(f"round {i+1}")

        p1_dart_y = random.randrange(0, 700)
        p1_dart_x = random.randrange(0, 700)
        p1_distance_from_center = math.hypot(center-p1_dart_x, center-p1_dart_y) #the distance formula
        # is_in_circle = distance_from_center <= width/2 #screen width
        if p1_distance_from_center <= 340:
            is_in_circle = True
            pygame.draw.circle(screen, "red", (p1_dart_x, p1_dart_y), 10)
            print("    player red: hit")
            p1_score=p1_score+1
        else:
            is_in_circle = False
            pygame.draw.circle(screen, "black", (p1_dart_x, p1_dart_y), 10)
            print("    player red: miss")

        pygame.display.flip()
        pygame.time.wait(1000)

        p2_dart_y = random.randrange(0, 700)
        p2_dart_x = random.randrange(0, 700)
        p2_distance_from_center = math.hypot(center-p2_dart_x, center-p2_dart_y) #the distance formula
        # is_in_circle = distance_from_center <= width/2 #screen width
        if p2_distance_from_center <= 340:
            is_in_circle = True
            pygame.draw.circle(screen, "blue", (p2_dart_x, p2_dart_y), 10)
            print("    player blue: hit")
            p2_score=p2_score+1
        else:
            is_in_circle = False
            pygame.draw.circle(screen, "grey", (p2_dart_x, p2_dart_y), 10)
            print("    player blue: miss")

        pygame.display.flip()
        pygame.time.wait(1000)

    if (p1_score > p2_score and guess == "red") or (p2_score > p1_score and guess == "blue"):
        text = font.render("your bet won", True, "black")
    else:
        text = font.render("your bet lost", True, "black")

    screen.fill("white")
    screen.blit(text, (100, 100)) # where <x> and<y> are coordinates on screen
    pygame.display.flip()
    pygame.time.wait(3000)
    darts = False

pygame.display.quit()

