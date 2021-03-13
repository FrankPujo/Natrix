import sys

# function assign a variable
def parseAssignVar( content ):
	tokens = content.split( " " )
	identifier = tokens[1]
	i = 3
	if tokens[i].isdigit():
		value = int ( tokens[i] )
	else:
		value = ""
		for i in range( len( tokens ) ):
			if i != 0 and i != 1 and i != 2:
				value += tokens[i]
				value += " "
		value = value.lstrip("\"").rstrip(" ").rstrip("\"")
	memory[ identifier ] = value

# read and prepare source code from chosen file
filename = sys.argv[1]
sourceCode = open(filename,'r').read()
sourceCode = sourceCode.replace( "\n", "" ).replace( "\t", "" )

# divide code in lines by semicolons
lines = sourceCode.split( ";" )

# variables memory
memory = {}

# read lin by line
for line in lines:
	tokens = line.split( " " )
	firstToken = tokens[0]
	if firstToken == "loc" and tokens[2] == "=":
		parseAssignVar( line )
	elif firstToken == "^":
		continue
	#elif firstToken == "print":
		#printStatement()

# check all the stored variables
print( memory )