""" 
Aim - Identify the Algorithm and Develop a dice simulator.

Algorithm:
1. Import Random Package.
2. Create a condition for Looping within the range of 1 to 6.
3. Print the Face.
"""

#Solution:
import random
print("Welcome to My Dice Simulator.")
x="y"
while x=="y":
    number=random.randint(1,6)
    if number==1:
        print("----------")
        print("|        |")
        print("|   0    |")
        print("|        |")
        print("----------")

    if number==2:
        print("----------")
        print("|        |")
        print("|  0  0  |")
        print("|        |")
        print("----------")

    if number==3:
        print("---------")
        print("|       |")
        print("| 0 0 0 |")
        print("|       |")
        print("---------")

    if number==4:
        print("----------")
        print("| 0    0 |")
        print("|        |")
        print("| 0    0 |")
        print("----------")

    if number==5:
        print("---------")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("---------")

    if number==6:
        print("---------")
        print("| 0 0 0 |")
        print("| 0 0 0 |")
        print("| 0 0 0 |")
        print("---------")


    x=input("Press 'y' to roll again & 'n' to stop simulation.")
print("Thank you for playing.")

"""
Developed by Ahamed Basha N.
"""