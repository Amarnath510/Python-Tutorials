"""
String and Substring
"""

name = "Amarnath"
print(name)

#substring
print("Print 0th character = " + name[0])
print("Print 1 to 3 characters = " + name[0 : 3])

#Update the string
new_name = name[0 : 3] + "Python"
print("Append name[0 : 3] with string Python = " + new_name)

# Triple quotes - Suppose you want to write on multiple lines.
statement = """amarnath is from Vijayawada and living in Bangalore currently
He will be continue to work here as along as he wishes.
"""
print(statement)

length_name = len(name)
length_stmt = len(statement)
print("Length_name = " + str(length_name) + " and length_stmt = " + str(length_stmt))

print(name.lower())
print(name.upper())

"""
How to update a string

Steps: 
	- Convert the string to a list
	- Now you have a grip of all the characters in the String. 
	- Update them as needed.

Example is to convert all characters from lower to upper and upper to lower.
"""
inp = "AmarNaTH"
inp_list = list(inp)
for i in range(0, len(inp_list)):
	ch = inp_list[i]
	if(ch.isupper()):
		inp_list[i] = ch.lower()
	elif(ch.islower()):
		inp_list[i] = ch.upper()

# finally convert back the list to string
inp = ''.join(inp_list)
print (inp)			