#!/bin/python
import os


options = "1. Display the default gateway \n2. Test Local Connectivity \n3. Test Remote Connectivity \n4. Test DNS Resolution \n5. Exit"

userInput = 0

while (userInput != 5):
    userInput = int(input("What would you like to do? \n" + options + "\n"))

    if userInput == 1:
        gateway = os.system("ip r | head -1").split()[2]
        print("Your default gateway is: " + str(gateway))

