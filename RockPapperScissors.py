
    # ROCK PAPPER SCICCOR

import random

print("-----welcome-----")

user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name: ")
print("hi:)", name)
print("""
Game RUles:
1) Papper Vs Rock --> Papper
2) Rock Vs Scissors --> Rock
3) Scissors Vs Papper --> Scissors""")
print()
while True:
    print("""choose one
        1) Rock
        2) Papper
        3) Scissors""")

    choice = int(input("Enter your choice from 1-3:"))
    print()
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input"))

    if choice == 1:
        user_choice = "Rock"
    elif choice ==2 :
        user_choice = "Papper"
    else:
        user_choice = "Scissors"
    print("user choice is:--->",user_choice)
    print("Now it is computer turn:-")

    computer = random.randint(1,3)

    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Papper"
    else:
        comp_choice = "Scissors"

    print("The computer's choice is:---> ", comp_choice)

    if((user_choice == "Papper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "papper")):
        print("Papper wins")
        result = "Papper"
    elif((user_choice == "Scissors" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissors")):
        print("Rock wins")
        result = "Rock"
    elif( user_choice == comp_choice):
        print(" TIE ")
        result = "tie"
    else:
        print("Scissors wins")
        result = "Scissors"

    if result == "Tie":
        ties += 1
    elif result == user_choice:
        user_score += 1
    else:
        comp_score += 1

    print("score are: ")
    print(name, "'s score is ", user_score)
    print("computers score is", comp_score)
    print("TIEs are ", ties)

    repeat = input("do you want to play again?")
    if repeat == "No" or repeat== "no":
        break

print("game over:)")

