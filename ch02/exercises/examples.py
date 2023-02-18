#bool - boolean value
#true/false
# - caps are important

#true, 1, "Hello"

print(type(True))

print(bool(1), bool (-1), bool("hello"))

print(bool(0), bool(''), bool([]))


#boolen expressions

x = 5
y = 1

print(x==y) #equality, == boolean equality test, = is assignment
print(x > y)
print(x < y)
print(x >= y) #=> - ERROR!
print(x <= y) #<= - ERROR!

#and, or, not - semantic operators

#and: and == True, when x and y are both True

print(True and True) #true
print(True and False) #false
print(False and True)
print(False and False)

# or - at least one True
print(True and True) #true
print(True and False) #true
print(False and True) #true
print(False and False) #false

# not- negation 

print(not True) #false
print("apple" == "apple")
print("apple" < "apple pie")
print(ord("a"), ord("A"))

print(1 is int)
print (1 is 1)

mynums = [1,2,3,4,5,6,7]
print(1 in mynums)
print(10 in mynums)

a= int(input("num"))

#if a < 0: #colon
#    a= abs(a) #indentation

#else: #no condition, always optional
#    print("positive")

print(a) #de-indentation to end the if statement

a = int(input("num:"))
if a > 5:
    print ("x is greater than 5")
    if a > 10:
        print("x is greater than 10")

else:
    print("x is less than or equal to 5")
#elif
#always goes between the if and else



need to finish this part but it on the phone
--------------------------------------------------------



# if <bollean condition>: #required
#   #do something
#elif <boolean condition>: #optional
#   #do something
#else: #optional
#   #do something



### Fizzbuzz

# - loop though a range of vlaues supplied by the user 
# - for each value in the range
# - if the value is divisible by 3, print "fizz"
# - if the value is divisible by 5, print "buzz"
# - if the value is divisible by 3 and 5, print "fizzbuzz"


num= int(input("enter an upper limit:"))
for i in range (num+1):
    #if not i % 3:
    if i % 3 == 0:
        print("fizz")

    