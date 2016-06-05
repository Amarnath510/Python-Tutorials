"""
Dictionary
	Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. 
	An empty dictionary without any items is written with just two curly braces, like this: {}

	Value can be any type but key should be of immutable data type such as strings, numbers, tuples.
"""

dict_ex = {'name' : 'amarnath', 'company' : 'Oracle'}

#length
print("Length of dictionary is = " + str(len(dict_ex)))

#print
#print(dict_ex['name'])
#print(dict_ex['company'])

# we will try with loop
for key in dict_ex.keys():
	print(dict_ex[key])

# Update values
dict_ex['company'] = 'Honey Well'	

# print again
for key in dict_ex.keys():
	print(dict_ex[key])

# print type of the dictionary
print("Variable type = " + str(type(dict_ex)))

# Compare two dictionaries - Compares all the keys and values.
# cmp(dict_1, dict_2)
# 0 if both of them are same
# 1 if dict_1 is > dict_2
# -1 if dict_1 is < dict_2
dict_1 = {'name' : 'Amarnath'}
dict_2 = {'name' : 'Sushma'}
dict_3 = {'name' : 'Amarnath'}

print(cmp(dict_1, dict_2))
print(cmp(dict_1, dict_3))