"""
Arthimetic Operators - We have alraedy these (+, -, *, /, %)
"""

"""
Comparison Operators
	==, !=, <> (assuming two values are not equal), >, <, >=, <=
"""

"""
Assignment Operators
	=, +=, -=, *=, /=, %=, **=, //=
"""

"""
Bitwise Operators - Bitwise operator works on bits and performs bit by bit operation.
	Operators are, &(AND), |(OR), ^(XOR), ~(Complement), <<(left shift), >>(right shift)
"""
a = 60 # 0011 1100
b = 13 # 0000 1101

print(a&b)
print(a|b)
print(a^b)
print(~a)
"""
Membership Operators - "in" and "not in"
"""
list = [1, 2, 3, 4, 5]
search = 10

if(search in list):
	print(str(search) + " is present in the list")
else:
	print(str(search) + " is NOT present in the list")

"""
Identity Operators - Identity operators compare the memory locations of two objects.
	2 types,
		1) is - Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
		2) is not - Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.
"""

a = 10
b = 10

if(a is b):
	print(str(a) + " has same identity as b " + str(b))
else:
	print(str(a) + " DO NOT have same identity as b " + str(b))	

b = 20
if(a is b):
	print(str(a) + " has same identity as b " + str(b))
else:
	print(str(a) + " DO NOT have same identity as b " + str(b))	