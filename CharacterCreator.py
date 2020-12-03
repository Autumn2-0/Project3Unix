#!/usr/bin/env python
import os
import shutil

#character creator class
#implements the character creator class


#character class - (includes but not limited to)
#	create - creates character
#	newCharacteroptions - after new character created
#	modify - modify character file
#	changecharactersname - change the name of the character thus changing the file name
#	deletecharacter - delete a character
#	listallCharacters - lists all character files


#Remember to implement a way so it reads from directory of program

#First do a command to find the base file
#Start search at home
#Then make current dir equal to the found directory 

#changechactername - os.rename


# print os.getcwd() - current work directory
# os.system() - use a shell command move to correct dir?

#information of modify commands
def help():
	print('add = add information to the end of the line')
	print('replace = change information already in place')
	print('erase = get rid of the entire line')
	print('skip = leave line as is\n')
	
def complete(vertify):
	vertify = input('Are you done with your edits? (Type Yes or No)')
	
	if(vertify == 'Yes' or vertify == 'No'):
		return vertify
		
	else:
		vertify = complete(vertify)

	

#modifies the .txt file through strings
def lineeditor(line):
	
	print('Current information:', line)
	option = input('What action would you like to perform? (Enter add, replace, erase, skip, or help for more information)')
	line = line.replace('\n', '')
	
	#adds words
	if(option == "add"):
		
		if(line == " "):
			line = input('Type what you would like to add:')
			
		else:
			line += input('Type what you would like to add:')

		#may need to add a new line
		print('Line now reads:', line)
	
	#replaces info
	elif(option == "replace"):
		change1 = input('Type what you would like to change:')
		change2 = input('Type what you like to replace it with:')
		line = line.replace(change1, change2)
		print('Line now reads:', line)
	
	#erases line
	elif(option == "erase"):
		line = ' '
		print('Line is now erased')

	#brings up help line
	elif(option == "help"):
		help()
		line = lineeditor(line)
		
	elif(option == "skip"):
		return line
		
	else:
		print('You did not enter a valid command.')
		line = lineeditor(line)
		
	#asks if user is done
	done = " "
	done = complete(done)
	
	if(done == 'No'):
		line = lineeditor(line)
	
	else:
		return line
		


#create character
def create():
	#ask for character name
	firstname = input('Characters first name: ')
	
	#confirm the name
	print('Type Y to confirm the name is', firstname)
	correct = input()
	
	if correct == "Y" or correct == "y":
		filename = "Characters/" + firstname + ".txt"
		
		#check if there already is a file with that name?
		
		#creates file and copies contents of base file
		open(filename, 'a').close()
		copycontent = shutil.copy('Characterbase.txt', filename)
		print('File', firstname + ".txt", 'created!')
		
	else:
		create()
	
#modify character
def modify():
	#ask for character name
	firstname = input('Characters first name:')
	filename = "Characters/" + firstname + ".txt";
	
	#searches for file
	if os.path.exists(filename):
		
		filelines = []                             	 # Create empty list
		with open (filename, 'rt') as characterfile: # Open .txt file
			for fileline in characterfile:           # Store each line in list
				filelines.append(fileline)    
			
			#Then go though a for loop for each section of the list
			newlist = []
			for x in filelines:
		
				#If a list element does not start with [#], it is editable
				if x[0] == '[' and x[1].isdigit() and x[2] == ']':
					newline = x.replace('\n', '')
					newlist.append(newline)
					print(x)
				
				else:
					#is editable
					newline = lineeditor(x)
					newlist.append(newline)
					
			filelines = newlist
			
			#once end of file reached, say so
			print('End of the file reached')
			characterfile.close()
			
		with open (filename, 'w') as newfile:
			for line in filelines:
				newfile.write('%s\n' % line)
			newfile.close()
		
		
	else:
		print('Error: File not found', firstname + ".txt")

#delete character
def deletecharacter():
	#ask for character name
	firstname = input('Characters first name:')
	filename = "Characters/" + firstname + ".txt";
	
	#searches for file
	if os.path.exists(filename):
	
		#asks if user is sure
		print('Press Y if you would like to delete the character', firstname)
		correct = input()

		#If Y pressed, delete file (UNIX delete)
		if correct == "Y" or correct == "y":
			#delete
			os.remove(filename)
			print(firstname + ".txt", 'has been deleted.')
		
	else:
		print('Error: File', firstname + ".txt", 'not found')
	
def listallCharacters():
	#lists out all file names
	directory = os.getcwd()
	print(os.listdir(directory + '/Characters'))
	
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
			1: "Create",
			2: "Modify",
            3: "Delete",
            4: "List",
            5: "Thank you for using the creator!"
			}
		return(switcher.get(selection, "Invalid option!"))



#start of the main function
selection = int(0)

print('Welcome to the Character Creator!')

while (selection != 5):
	printOptions() #Displays options
	selection = int(input())
	choice = switch_demo(selection)
	
	if(choice == "Create"):
		create()
		
	elif(choice == "Modify"):
		modify()
		
	elif(choice == "Delete"):
		deletecharacter()
		
	elif(choice == "List"):
		listallCharacters()
		
	else:
		print(choice)
		
