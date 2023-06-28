import random
import art
print(art.logo)
print("welcome to the Number Guessing Game ")
print("i am thinking of a number between 1 to 100")
print("Choose a difficulty level easy or hard")
THE_NUMBER=random.randint(1,100)
input_n=input()
if input_n=="easy":
    attempts=10
    print("you have 10 attempts to guess the number")
    while attempts>0:
        guessed=int(input())
        if guessed==THE_NUMBER:
            print("you got the number")
            break
        elif guessed<THE_NUMBER:
            print("too low")
        else:
            print("too high")
        attempts-=1
elif input_n=="hard":
    attempts=5
    print("you have 5 attempts to guess the number")
    while attempts>0:
        guessed=int(input())
        if guessed==THE_NUMBER:
            print("you got the number")
            break
        elif guessed<THE_NUMBER:
            print("too low")
        else:
            print("too high")
        attempts-=1