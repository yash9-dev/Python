import os
os.system('cls')

global bill
print("Welcome to the Yash Pizza Deliveries!")
size = input("What should be the size of the pizza? S , M , L: ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
cheese = input("Would you like some extra cheese ? Y or N : " )
if(cheese == 'y' or 'Y'):
    bill = bill+5
else:
    bill
pepronni = input("Would you like to add pepronni ? Y or N : ")
if(pepronni == 'y' or 'Y'):
    bill = bill+3
else:
    bill
print(f"Your Final bill is ${bill}")

