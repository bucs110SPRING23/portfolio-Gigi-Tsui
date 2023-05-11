import pygame

#part A
def threenp1(n):
    count = 0
    while n > 1:
        count = count + 1
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int((n*3)+1)
    
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for n in range (2, upper_limit + 1):
        objs_in_sequence[n]=threenp1(n)
    return objs_in_sequence

def main():
    pygame.init()
    upper_limit=int(input("enter the limit number:"))
    results = threenp1range(upper_limit)
    graph_coordinates(results)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()


#part B

def graph_coordinates(threenplus1_iters_dict):
    window=pygame.display.set_mode ((600,600))
    window.fill("white")
    coordinates = [(2*x,500-y) for (x,y) in threenplus1_iters_dict.items()]

    if len(coordinates)>=2:
        pygame.draw.lines(window, "black", False, coordinates)


    # new_display = pygame.transform.flip(window, False, True)
    # (width, height) = new_display.get_size()
    # new_display = pygame.transform.scale(window, (width * 5, height * 5))
    # window.blit(new_display, (600,600))


    iters_threenplus1_iters_dict = [tup[1] for tup in threenplus1_iters_dict.items()]
    print(iters_threenplus1_iters_dict)

    # for i in range(len(coordinates)):
    #     if iters_threenplus1_iters_dict[i] > max_so_far:
    #         max_so_far=iters_threenplus1_iters_dict[i]


    max_so_far = max(iters_threenplus1_iters_dict)
    font = pygame.font.Font(None, 50)
    msg = font.render(f"max_so_far: {max_so_far}", True, ("green"))
    window.blit(msg, (10,10))

main()
     



