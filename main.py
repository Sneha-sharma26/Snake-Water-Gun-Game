import random

comp_choice = random.choice(["snake","water","gun"])
user_choice= input("Enter your choice out of snake/water/gun : ")
user_choice.lower()
print(f"Computer chose: {comp_choice}")
print(f"You chose: {user_choice}")

if (user_choice == comp_choice):
    print("It\'s a draw!")

else:
    if (user_choice == "snake" and comp_choice == "water"):
        print("You won!!")
    elif (user_choice == "snake" and comp_choice == "gun"):
        print("Computer won!!")
    elif (user_choice == "water" and comp_choice == "snake"):
        print("Computer won!!")
    elif (user_choice == "water" and comp_choice == "gun"):
        print("You won!!")
    elif (user_choice == "gun" and comp_choice == "snake"):
        print("You won!!")
    elif (user_choice == "gun" and comp_choice == "water"):
        print("Computer won!!")
    else:
        print("Something went wrong.")
    