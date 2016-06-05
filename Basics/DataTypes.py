"""
Standard Data Types:

1) Numbers - int, long, float, complex
2) String
3) List
4) Tuple
5) Dictionary
"""

"""
Numbers
"""
print("***** Numbers *****")
var_int 	= 10
print(var_int)

var_float	= 0.0 #or 15.20
print(var_float)

var_long	= 51924361L
print(var_long)

var_complex	= 3.14j
print(var_complex)


"""
Strings - String is nothing but a continous set of characters.
"""
print("***** Strings *****")
var_str 	= "amarnath"
print(var_str)

var_str_0 	= var_str[0] 		#first character of the string
print(var_str_0)

var_str_2_5 = var_str[2 : 5] 	#Sub String from 3 to 5
print(var_str_2_5)

var_str_2_ 	= var_str[2 : ]		#Substring starting from 3 to end
print(var_str_2_)

var_str_double = var_str * 2	#String repeated two times
print(var_str_double)

var_str_append = var_str + "TEST" #Append TEST to string
print(var_str_append)


"""
Lists - A list contains items separated by commas and enclosed within square brackets []
To some extent, lists are similar to arrays in C. One difference between them is that all the items belonging to a list can 
be of different data type.

How do we access? 
We access them using [] or [:]
"""
print("***** Lists *****")
_list = ['amarnath', 7259, 'chandana', 10.23]
tiny_list = ['Puppy', 420]

print _list

# get xth index element
print _list[0]

# get index out of range. List is actually 4 that is 0 .. 3 so we will try for 4.
#print _list[4] # we will get out of range exception

print _list[0 : 3] # Prints elements from 1 to 3

print _list[0 : 3] # Prints elements from 1 to end

print tiny_list * 2 # Prints list two times

print _list + tiny_list # Prints concatenated lists.


"""
Tuples: Similar to list just a sequence of data. But lists are enclosed in [] where as Tuples are enclosed in ()
Main difference between list and tuples other than enclosing brackets is, Tuples cannot be upated. In simple Tuples are read only lists.
"""
print("***** Tuples *****")
tuple = ('abcd', 1234, 'xyz')
print(tuple)
# other operations are same just liek lists.

# we will check the difference between Tuples and list.
#tuple [2] = 'amarnath' # TypeError: 'tuple' object does not support item assignment
_list[2] = 'amarnath'

"""
Dictionary: These are like Hash table. They work like associative arrays.
A dictionary 
		key can be almost any python type but are usually numbers or strings.
		Values on the other hand can be any arbitary Python object.
"""
print("***** Dictionary *****")
dict = {}
dict ['one'] = "This is one"
dict [2] = 'This is 2'

tiny_dict = {'name' : 'amarnath', 'code' : 46460, 'dept' : 'CSE'}

print(dict['one'])
print(dict[2])
print(tiny_dict)
print(tiny_dict.keys())
print(tiny_dict.values())
