#Character creator main file

#runs character creator

#!/usr/bin/env python

#prints message
#   Please choose a command:
#	1. Create a character
#	2. Modify a character
#	3. Delete a character
#	4. List characters
#	5. Exit

#main function with selections

#prints the options
def printOptions():

	print('Please choose a command:')
	print(' ')
	print('1. Create a character')
	print('2. Modify a character')
	print('3. Delete a character')
	print('4. List characters')
	print('5. Exit')
	print(' ')
	print('Enter your selection:')

#determines which option was selected
def switch_demo(selection):
		switcher = {
			1: create(),
			#2: modify(),
            #3: deletecharacter(),
            #4: listallCharacters(),
            5: "Thank you for using the creator!"
			}
		print(switcher.get(selection, "Invalid option!"))


selection = int(0)

print('Welcome to the Character Creator!')

while (selection != 5):
	printOptions() #Displays options
	selection = int(input())
	switch_demo(selection)
			