def foo (param1, param2):
    return param1+param2

def bar(param1=4, param2=3): #default values, named params
    local_var = 5
    return param1+param2

#local_var=5 means scope is limited to the function

#def bar(param1=4, param2=3): #default values, named params
    #if True:
        #return param1+param2 #return ends function
    #else:
        #pass #kepp going

#foo(1,2) #have to put it all the param in order or it wont work

#bar(1)
#bar()
#bar(1,3)

result = bar(param2=1, param1=2)
print(result)


def percentage_to_letter(percent=99):
    let = "A"
    if 80 < percent < 90:
        let = "B"
    elif 70 < percent <80:
        let = "C"
    elif 60 < percent <70:
        let = "D"
    elif percent < 60:
        let = "F" 
    return let

def is_passing(letter):
     """ 
     this is a function that retuens a letter grade based on a percentage:
     args: percent (int) 
     return: letter (str)
     """
     return letter.lower() in "abc"

#def main(): #driver code
    #letter = percentage_to_letter(90)
    #if is_passing(letter):
        #print("You passed!")
    #else:
        #print("someone messed up your grades!")

def main():
    grades =[90, 80, 70, 60, 50]
    for grade in grades:
        letter = percentage_to_letter(grade)
    if is_passing(letter):
        print ("You passed!")
    else:
        print ("someone messed up your grades")

main()


print()


#for loop kinda a wild loop - programming pattern
#there are several programming pattern
## accumulator pattern

result = 0
for i in range(10):
    result= result +i

print(result)


def remove_vowels(string):
    vowels = "aeiou"
    vowels += vowels.upper()
    result = ""
    for ch in string:
        if ch not in vowels:
            results += ch
    return result


def main():
    mystring = "Hello World"
    mystring = remove_vowels(mystring)
    print(mystring)

main()