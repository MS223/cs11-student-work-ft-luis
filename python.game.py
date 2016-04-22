name = raw_input("What's your name? ") #The first line is to get the name of the user
upper_bound = input("What's the highest number you want to guess?") #This line asks what the capacity is.
import random #Randomizes the integers
random_number = random.randint(0, upper_bound)#Sets the bound of the integers
guess = input("What is your guess?") #Lets the userguess what integer the computer os thinking of

while guess != random_number:
    guess = input("What is your guess?")

print ("Congrats") 
