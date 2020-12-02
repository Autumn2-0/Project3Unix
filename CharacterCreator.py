#character creator class


#implements the character creator class


#character class - (includes but not limited to)
#	create - creates character
#	newCharacteroptions - after new character created
#	modify - modify character file
#	deletecharacter - delete a character
#	listallCharacters - lists all character files

#class CharacterCreator:

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
		#could use UNIX commands here (find, copy, rename)
		
	else:
		create( )
		
def modify():
	#ask for character name
	firstname = raw_input('Characters first name:')
	filename = firstname + ".txt";
	
	#finds file (use UNIX find)
	#if file not found, print message saying say so
	
	#opens file if file exists
	charfile = open(filename, 'w') 
	
	#reads off lines with [#]
	#lets user type in or skip
	#updates as it goes
	
	#once end of file reached, say so 
	#close file
	
def deletecharacter():
	#ask for character name
	firstname = raw_input('Characters first name:')
	filename = firstname + ".txt";
	
	#finds file (use UNIX find)
	#if file not found, print message saying say so
	
	#asks if user is sure
	print 'Press Y if you would like to delete the character', firstname
	correct = raw_input()

	#If Y pressed, delete file (UNIX delete)
	if correct == "Y":
		#delete

	
def listallCharacters():
	#lists out all file names
	#find all files in folder and print out names