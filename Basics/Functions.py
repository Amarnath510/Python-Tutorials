"""
Functions
"""

"""
Function without return statement
"""
def printName(str):
	print(str)
	return #optional

printName('Amarnath')

########################################

"""
Print the list
"""

def printList(list):
	for item in list:
		print(item),
	return
	
list_ex = [1, 2, 3, 4]
printList(list_ex)

"""
Pass by reference
Here, we are maintaining reference of the passed object and appending values in the same object.
"""
def passByReference(list):
	list.append(5)
	return
print("\n***** Pass by Reference tutorial *****")
list_reference = [1, 2, 3, 4]
print("Before passing to function " + str(list_reference))
passByReference(list_reference)	
print("After passing to function " + str(list_reference))

"""
Pass by value
"""
print("\n***** Pass by Value tutorial *****")
def passByValue(list):
	list = [10, 20, 30]
	print("List local to the function " + str(list))
	return

list_value = [1, 2, 3]
print("Before the function " + str(list_value))
passByValue(list_value)
print("After the function call " + str(list_value))


"""
Function Arguments Types
1) Required Arguments
2) Keyword Arguments
3) Default Arguments
4) Variable-Length Arguments
"""

# Required Arguments - Required arguments are the arguments passed to a function in correct positional order.

def printStudent(name, age, msg):
	print("**** " + msg + " ****")
	print(name + " " + str(age))
	return

printStudent('Amarnath', 29, "Required Arguments Call")
# printStudent(29, 'Amarnath') - Won't work since the parameters are different.

# Keyword Arguments - Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name. So above method can be fixed by stating the parameter name.
printStudent(age = 29, name = 'Amarnath', msg = 'Keyword Arguments Call')


# Default Argument - A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.
# In the below example, in the printEmployee function we are not passing any age so it will take the default value.
# Default argument parameter should always be the last element.
def printEmployee(name, msg, age = 30):
	print("**** " + msg + " ****")
	print(name + " " + str(age))
	return

printEmployee('amarnath', "Default Arguments tutorial")	
# If we pass age then it won't take the default value.
printEmployee('amarnath', "Default Arguments tutorial", 100)	

"""
Variable-Length Arguments - You may need to process a function for more arguments than you specified while defining the function.
 def functionname([formal_args,] *var_args_tuple ):
 where, formal_args are normal ones and should be icoming before the variable arguments
 		and asterisk indicates the that the variable is variable length variable.
"""
def printNumbers(arg1, *args):
	print(arg1)
	for var in args:
		print(var)
	return	

printNumbers(1, 2, 3, 4, 5)


"""
Anonymous function - We need to use Lambda function to declare a anonymous function.
	1) Anonymous function deos not have any standard manner by using def keyword. 
	2) Lambda function can take any number of arguments but returns one value in terms of expression.
	3) An anonymous function cannot be a direct call to print because lambda requires an expression.
	4) Lambda function has their own namespace and cannot access any variables other than those in the parameter list.
"""
print("Anonymous Function Tutorial")
sum = lambda arg1, arg2 : arg1 + arg2
print("Anonymous Funtion Tutorial = " + str(sum(10, 20)))

"""
return statement
"""

def sumofNum(a, b):
	return a + b

print("Return statement Example = " + str(sumofNum(100, 200)))