#character creator class

import os
import shutil
#implements the character creator class


#character class - (includes but not limited to)
#	create - creates character
#	newCharacteroptions - after new character created
#	modify - modify character file
#	changecharactersname - change the name of the character thus changing the file name
#	deletecharacter - delete a character
#	listallCharacters - lists all character files

#class CharacterCreator:
#Remember to implement a way so it reads from directory of program
#Make a folder for characters?

#Maybe first do a command to find the base file
#Start search at home
#Then make current dir the dir it is found in 

#changechactername - os.rename


# print os.getcwd() - current work directory
# os.system() - use a shell command move to correct dir?



#create character
def create():
	#ask for character name
	firstname = raw_input('Characters first name:')
	
	#confirm the name
	print 'Type Y to confirm the name is', firstname
	correct = raw_input()
	
	if correct == "Y":
		filename = firstname + ".txt"
		
		#check if there already is a file with that name?
		#copies base file and renames with character name
		#could maybe use UNIX commands here (find, copy, rename)
		open(filename, 'a').close()
		print shutil.copy('Characterbase.txt', filename)	
		
	else:
		create( )
		
def modify():
	#ask for character name
	firstname = raw_input('Characters first name:')
	filename = firstname + ".txt";
	
	#searches for file
	if os.path.exists(filename):
	
		#opens file if file exists
		charfile = open(filename, 'w') 
	
		#reads off lines with [#]
		#displays what is already written too - this needs to be editable
		#lets user type in or skip
		#updates as it goes
	
		#once end of file reached, say so
		print 'End of the file reached'
		
		#close file
		
	else:
		print 'Error: File not found', filename
	
def deletecharacter():
	#ask for character name
	firstname = raw_input('Characters first name:')
	filename = firstname + ".txt";
	
	#searches for file
	if os.path.exists(filename):
	
		#asks if user is sure
		print 'Press Y if you would like to delete the character', firstname
		correct = raw_input()

		#If Y pressed, delete file (UNIX delete)
		if correct == "Y":
		#delete
		
	else:
		print 'Error: File not found', filename

	
def listallCharacters():
	#lists out all file names
	#find all files in folder and print out names