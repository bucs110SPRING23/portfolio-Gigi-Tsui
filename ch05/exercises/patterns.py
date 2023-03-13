def star_pyramid(rows):
    for i in range (1, rows + 1):
        print("*" + 1)


def rstar_pyramid(rows):
    for i in range (rows,0 ,1 - 1):
        print("*" + 1)


levels = (input("what is pyramid height:"))

star_pyramid(levels)
rstar_pyramid(levels)