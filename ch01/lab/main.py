#Part B
import random
number = random.randint(1,10)
print(number)

A = [0, "t", 556.8, 68, 0]
B= random.choice(A) 
print(B)

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print ("cost per week:", cost_per_week)

classes_per_week = (weeks / classes)
print ("classes per week", classes_per_week)

cost_per_class = (cost_per_week / classes_per_week)
print ("cost per class", cost_per_class)






