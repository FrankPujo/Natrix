import sys

# check if reading a function or a loop
inFunct = False
inLoop = False

# assign a value to a variable
def parseAssignVar( content ):
	tokens = content.split( " " )
	identifier = tokens[1]
	if tokens[3].isdigit():
		operation = ""
		for i in range( len( tokens ) ):
			if i != 0 and i != 1 and i != 2:
				operation += tokens[i]
		value = eval( operation )
	elif tokens[3][:1] == "\"":
		value = ""
		for i in range( len( tokens ) ):
			if i != 0 and i != 1 and i != 2:
				value += tokens[i]
				value += " "
		value = value.lstrip("\"").rstrip(" ").rstrip("\"")
	elif memory[tokens[3]] is not None:
		if tokens[5] is not None:
			if tokens[5].isdigit():
				result = str(memory[tokens[3]]) + tokens[4] + tokens[5]
				value = eval( result )
			elif memory[tokens[5]] is not None:
				result = str(memory[tokens[3]]) + tokens[4] + str(memory[tokens[5]])
				value = eval( result )

		else:
			value = memory[tokens[3]]
	memory[ identifier ] = value

# print statement
def printStatement( content ):
	stuff = content[6:]
	
	if stuff[:1] == "\"":
		print( stuff[1:-1] )
	else:
		print( memory[ stuff ] )

# parse for loops
def startLoop( content ):
	inLoop = True
	tokens = content.split( " " )
	repeating = memory[ tokens[1] ]
	print( repeating )

# read and prepare source code from chosen file
filename = sys.argv[1]
sourceCode = open(filename,'r').read()
sourceCode = sourceCode.replace( "\n", "" ).replace( "\t", "" )

# divide code in lines by semicolons
lines = sourceCode.split( ";" )

# variables memory
memory = {}

# temporarily store functions and loops contents
tempFunct = ""
tempLoop = ""

# read line by line and call functions for each
for line in lines:
	tokens = line.split( " " )
	firstToken = tokens[0]

	if firstToken == "^":
		continue

	if inLoop == True:
		print( "looping!" )
		continue

	if firstToken == "loc" and tokens[2] == "=":
		parseAssignVar( line )
	elif firstToken == "print":
		printStatement( line )
	elif firstToken == "loop" and tokens[2] == "for":
		startLoop( line )

# check all the stored variables
print( memory )