"""
Tuple - A tuple is a sequence of immutable Python objects. 
"""

tuple_ex = ('amarnath', 'chandana', 2000, 4000)
print(tuple_ex)

#length
print("Length of Tuple is: " + str(tuple_ex))

#get a particular index tuple value
print("Tuple at index 0 is " + tuple_ex[0])

# Update a tuple - It should fail.
#tuple_ex(1) = 'Sushma'

# Delete Tuple elements - You cannot delete any tuple element. You should delte whole tuple.
del tuple_ex

#length - Should throw error since we have delete it.
#print("Length of Tuple is: " + str(tuple_ex))

tuple_1, tuple_2 = (1234, 245, 'zara', 'abc'), (1, 2, 3, 4)
print("Max tuple_1 element is = " + max(tuple_1))
print("Min tuple_1 element is = " + str(min(tuple_1)))
print("Max tuple_2 element is = " + str(max(tuple_2)))
print("Min tuple_2 element is = " + str(min(tuple_2)))