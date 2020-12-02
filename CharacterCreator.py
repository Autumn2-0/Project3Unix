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