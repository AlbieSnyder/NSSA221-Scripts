#!/bin/python
import subprocess


options = "1. Display the default gateway \n2. Test Local Connectivity \n3. Test Remote Connectivity \n4. Test DNS Resolution \n5. Exit"

userInput = 0

while (userInput != 5):
	userTestInput =  input("What would you like to do? \n" + options + "\n")
	try:
		userInput = int(userTestInput)
	except:
		print("You have to choose one of the options!")
		userInput = 0
	if userInput == 1:
        	gateway = subprocess.check_output("ip r | head -1 | cut -d ' ' -f 3", shell=True)
            print("Your default gateway is: " + str(gateway)[2:-3])
	elif userInput == 2:
		try:
			subprocess.check_output("ping 0 -c 2", shell = True, stderr = subprocess.PIPE)
			print("The test passed")
		except subprocess.CalledProcessError as e:	
			print("The test failed")
    elif userInput == 3:
		try:
			subprocess.check_output("ping 8.8.8.8 -c 2", shell = True, stderr = subprocess.PIPE)
			print("The test passed")
		except subprocess.CalledProcessError as e:	
			print("The test failed")
	elif userInput == 4:
		try:
			subprocess.check_output("ping google.com -c 2", shell = True, stderr = subprocess.PIPE)
			print("The test passed")
		except subprocess.CalledProcessError as e:	
			print("The test failed")