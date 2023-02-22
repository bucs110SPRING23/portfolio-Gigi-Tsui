import random

num = print(random.randint(1,10))

for _ in range(3):
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == num: 
        print ("Correct! You Win. My number was", num)
    elif guess < num:
        print ("The number is lower")
    elif guess > num:
        print ("the number is higher,")
