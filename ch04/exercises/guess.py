import random
import math

number = int(random.randrange(1,1000))

guess = 0
guess_num = 0

while guess_num != number:
    guess = int(input("Guess a number between 1 and 1000 until you get it right: "))
    guess_num = guess_num +1
    if guess_num == number:
        print("good job guessing the number")
        break
    elif guess > number:
        print ("guess is too high")
    elif guess < number:
        print ("guess is too low")

print("the answer was:", number)
print("you took", guess_num, "tries")

#while: loop until a condition is met\
#   more control over the loop

#for loop 
    #a set # of duration like a certain amout
    #iterating over a collection

#for i in range()
    #if num>5 or num<1:
        #num = int(input(msg))
        
#msg= "enter a number between 1 and 5"

#num = int(input(msg))
#while num>100 or num<1:
        #num = int(input(msg))

print("done")