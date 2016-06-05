"""
Reading from keyboard:
	We have two functions,
		1) raw_input - Reads line from the STDIN and returns it as a string.
		2) input - Equivalent to raw_input, except that it assumes that the input is a valid Python expression and returns the evaluated result to the user. (See example below. An expression is given as input and it is evaluated and output is returned.)
"""
"""
name = raw_input("Enter name: ")
print("Entered name = " + name)


list = input("Enter the input: ")
print("Entered input expression is = ", list)
"""

"""
File operations:
Before reading/writing to a file we need to open it using open() function.
Ex: file object = open(file_name[, access_mode][, buffering])
	// do some operations and finally close.
	file.close()

access_modes = r, rb, r+, rb+, w, wb, w+, wb+
buffering = If set to 0 then no buffering takes place. If 1 then buffering is performed while accessing the file. If negative then buffer size is the system default.

We have methods such as, 
	file.closed 	- Returns true if file is closed.
	file.mode 		- Returns access mode if file was opened.
	file.name 		- Returns name of the file.
	file.softspace	- Returns false if space explicitly required.
"""

fo = open("sample.txt", "wb")
print("Name of the file is = " + fo.name)

# Writing to a file
stmt = "Hello Bangalore is becoming worst of its kind."
fo.write(stmt)
print("In " + fo.name + " data is written. Please refer it.")
#close the file after writing
fo.close()

# Open the file for reading
file_rd = open("sample.txt", "r+") # r+ is for both reading and writing.
data = file_rd.read(10) # here 10 means read 10 characters at a time. if you don't put it will read mostly until end of the file.
# data = file_rd.read()
print(data)


"""
Rename file
Delete file
Make Directory
Get current working directory
Remove directory
"""
# import os
# os.rename("source_file_name.extension", "destination_file_name.extension")
# os.remove(file_name.extension)
# os.mkdir("directory name")
# os.getcwd()
# os.rmdir("directory_name")