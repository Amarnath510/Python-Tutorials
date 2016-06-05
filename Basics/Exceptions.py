"""
Exception
	Two types,
		1) Exception Handling
		2) Assertions

"""

"""
Execption Handling:
	Exception - Base class for all exceptions.
	Arthimetic Error - For all errors occured for numeric type.
	Overflow error - 
	EOF error - 
	IO error - 
	Indentation Error - 


What is an Exception?
	An exception is an event, which occurs during the execution of a program that disrupts the normal flow of 
	the program's instructions.	
In Python we have try block, except block (like catch block in Java)
"""
print("\n***** Try/Except *****")
try:
	a = 10
	b = 0
	# b = raw_input("Enter b value: ")
	result = a / int(b)
	print("In try block")
except Exception:
	print("Error while doing division")
else:
	print("Division completed successfully.")

"""
except block may not have any exception stated also.
"""	
print("\n***** Try/Except without except definiton *****")
try:
	a = 10
	result = a / 0
	print("In try block")
except:
	print("Error while doing division")
else:
	print("Successfully completed execution")	

"""
We can also have multiple exceptions in the same line.
"""	
print("\n***** Try/Except with multiple exceptions on same line. *****")
try:
	a = 10
	b = 0
	result = a / b
	print("In try block")
except(ArithmeticError, EOFError):
	print("Error during divison operation")
else:
	print("Executed Successfully")	


"""
How to throw an exception?
Use "raise" to throw an exception.
NOTE: Always be specific while raising an exception.
"""
print("\n***** Try/Except with raise exceptions. *****")
def raiseException(level):
	try:
		if level < 10:
			raise ValueError("Invalid Level!")
		print ("You are at level = " + str(level))
	except Exception as error:
		print("Caught this error " + repr(error))
		

raiseException(10)
raiseException(1)	
