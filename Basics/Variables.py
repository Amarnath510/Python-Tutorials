"""
Based on the assigned value the interpreter allocates the memory and decides what can be stored in the reserved memory.
"""

print("\n**** Variable Assignment ****")
# Assigning values to variables
count = 10			# An integer is assigned
name = "Amarnath"	# An String is assigned
miles = 10.23		# An float is assigned

print(count)
print(name)
print(miles)


print("\n**** Multi Assignment ****")
# Multi assignment
a = b = c = 1
print(a)
print(b)
print(c)

print("\n**** Multi Assignemnt with different datatypes ****")
# Mutli assignment with different datatypes
a, b, c = 1, 2.12, "amarnath"
print(a)
print(b)
print(c)