import sys

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
	else:
		value = ""
		for i in range( len( tokens ) ):
			if i != 0 and i != 1 and i != 2:
				value += tokens[i]
				value += " "
		value = value.lstrip("\"").rstrip(" ").rstrip("\"")
	memory[ identifier ] = value

# print statement
def printStatement( content ):
	stuff = content[6:]
	
	if stuff[:1] == "\"":
		print( stuff[1:-1] )
	else:
		print( memory[ stuff ] )

# read and prepare source code from chosen file
filename = sys.argv[1]
sourceCode = open(filename,'r').read()
sourceCode = sourceCode.replace( "\n", "" ).replace( "\t", "" )

# divide code in lines by semicolons
lines = sourceCode.split( ";" )

# variables memory
memory = {}

# read line by line and call functions for each
for line in lines:
	tokens = line.split( " " )
	firstToken = tokens[0]
	if firstToken == "loc" and tokens[2] == "=":
		parseAssignVar( line )
	elif firstToken == "^":
		continue
	elif firstToken == "print":
		printStatement( line )

# check all the stored variables
# print( memory )