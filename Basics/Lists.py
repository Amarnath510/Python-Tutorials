"""
Iterate a list
"""
print("Printing Lists")
list_int = [1, 2, 3, 4, 5]

for x in list_int:
	print(x)

print("Length of a list = " + str(len(list_int)))
print("MAX of a list = " + str(max(list_int)))
print("MIN of a list = " + str(min(list_int)))


# insert, delete, update, sort
list_temp = []
print(list_temp)

# insert
list_temp.append('ama')
list_temp.append(2000)
print(list_temp)

#insert at particular index. insert(position, element)
list_temp.insert(0, 9999)
print(list_temp)

# delete
# count will count the occurence of the given element
print("Before deletion count is = " + str(list_temp.count(2000)))
list_temp.remove(2000)
print(list_temp)
print("Before deletion count is = " + str(list_temp.count(2000)))


# pop - Deletes element at a particular location. If the position is not given then pops the last element.
list_pop = [1, 2, 3, 4, 5]
print("Length of list_pop = " + str(len(list_pop)))
list_pop.pop()
print("Length of list_pop = " + str(len(list_pop)))
list_pop.pop(2)
print("Length of list_pop = " + str(len(list_pop)))

# Reverse the list
list_rev = [1, 2, 3, 4, 5]
print("Before list reverse = ", list_rev)
list_rev.reverse()
print("After list reverse = ", list_rev)

# Sort the list. You can also sort using sorted notation like .. sorted(list_sort)
list_sort = [5, 4, 3, 2, 1]
print("Before list sort = ", list_sort)
list_sort.sort()
print("Before list sort = ", list_sort)

# index will return the first occurence of the element's index
print("Index of element 3 is = " + str(list_sort.index(3)))


"""
Fixed size list

How to create a fixed size list.
"""
list_fixed = [None] * 5
for i in range(0, len(list_fixed)):
	print(list_fixed[i])