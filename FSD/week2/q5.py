password = "changeme"
correct = False
tries = 0
while correct != True and tries < 6:
	userInput = input("Type in your password: ")
	tries += 1
	if userInput == password:
		print("Accepted with", tries, "tries")
		break
	if tries == 5:
		print("Access denied, please press enter to exit and contact security to reset your password")
		exit = input()
		if len(exit) == 0:
			break
	