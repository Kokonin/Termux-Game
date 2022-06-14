import random
from secrets import choice
from time import sleep

def clearprint():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def main():
    rps = random.choices = ["Rock","Paper","Scissors"]
    print("Choose one: %s" %(rps))
    choose = input()
    x = random.choice(rps)
    if choose == "Rock" or "rock " or "r" or"R":
        print("Enemy Choice: " + x)
        if x == "Paper":
            print("You Lost!")
        elif x == "Rock":
            print("Tie!")
        elif x == "Scissors":
            print("You Won!")
    elif choose == "Paper" or "paper" or "p" or"P":
        print("Enemy Choice: " + x)
        if x == "Paper":
            print("Tie!")
        elif x == "Rock":
            print("You Won!")
        elif x == "Scissors":
            print("You Lost!")
    elif choose == "Scissors" or "scissors" or "s" or "S":
        print("Enemy Choice: " + x)
        if x == "Paper":
            print("You Won!")
        elif x == "Rock":
            print("You Lost!")
        elif x == "Scissors":
            print("Tie!")
    
    sleep(5)
    Repeat = input("Play Again? yes/no : ")
    if Repeat == "Yes" or "yes" or "y" or "y":
        clearprint()
        sleep(1)
        main()
    elif Repeat == "No" or "no" "n" "N":
        print("Bye!")
        sleep(2)
        clearprint()
        exit()
main()
