#part A
def threenp1(n):
    count=0
    while n !=1:
        if n % 2 == 0:
            n=n//2
        else:
            n = n*3+1
        count = count + 1
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for n in range (2, upper_limit + 1):
        objs_in_sequence[n]=threenp1(n)
    return objs_in_sequence

def main():
    threenp1_iters_dict=threenp1range(10)
    print(threenp1_iters_dict)

main()


#part B
import pygame

def graph_coordinates(threenplus1_iters_dict):
    pygame.init()
    display=pygame.display.set_mode((600,600))

    font = pygame.font.Font(None, 10)
    coordinates = [(x,y) for x,y in threenplus1_iters_dict.items()]
        
    pygame.draw.lines(display, ("Black", False, coordinates, 2))

    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 5, height * 5))

    max_so_far = max(threenplus1_iters_dict())
    msg = font.render(("max so far:", True, "green"))

    display.blit(msg, (10,10))

    pygame.display.flip()

main()


