import pygame 
pygame.init()
screen = pygame.display.set_mode()

dimensions = screen.get_size()
print(dimensions)

starting_point = (dimensions[0]//2, dimensions[1]//2)

#pygame.draw.circle(screen, "green", [200, 150],50)
#pygame.draw.circle(screen, "blue", [200, 220],60)
#pygame.draw.circle(screen, "purple", [200, 310],70)

radius= 200
for _ in range(3):
    pygame.draw.circle(screen, "red", starting_point, radius)
    radius = radius // 2 
    starting_point[1]= starting_point[1]-radius


pygame.display.flip()
pygame.time.wait(2000)



