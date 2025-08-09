import os
os.system('cls')
global choice1
global choice2
global choice3
print("Welcome to Treasure Island.\n Your mission is to find the Treasure. ")
choice1 = input("You're at a cross road. Where do you want to go?" \
"\nType 'left' or 'right':\n")
# print('Type "left" or "right"')
if(choice1 == "left"):
    choice2 = input('"swim" or "wait":')
else:
    print("Fall into a hole.\n Game over.")
if(choice2 == "swim"):
    print("Attacked by trout.\n Game over.")
else:
    choice3 = input("There are 3 doors infront of you. \n Red , Yellow , Blue. \n Which one you would choose?")
    if(choice3 == 'Red'):
        print("Burned by Fire.\n Game over.")
    if(choice3 == "Blue"):
        print("Eaten by beasts.\n Game over.")
    if(choice3 == "Yellow"):
        print(" Hurray! You Win !!")
    else:
        print("Game over.")
