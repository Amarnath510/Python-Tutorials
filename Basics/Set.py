"""
How to create a set
How to add elements to a set
Remove elements from set
print a set
How to convert a set to a list
Hot to sort a set
Union, Intersection of two sets
"""

def printSet(mySet, msg):
	print("*********   " + msg + "   **********")
	for item in mySet:
		print(item)

mySet = set()

# Add elements.
mySet.add(100)
mySet.add(2)
mySet.add(20)
mySet.add(30)
mySet.add(5)
mySet.add(1)

printSet(mySet, "All elements")

# Delete/Remove element
mySet.discard(20)
printSet(mySet, "All elements - after deleting element 20")

# Convert a set to a list
myList = list(mySet)
printSet(myList, "After converting set to list")

# Sort the set. You cannot sort the set we need to conver the set to a list 
# and then  sort the list
myList = sorted(myList)
printSet(myList, "After sorting list")

# Union of two sets
mySet_1 = set()
mySet_1.add(1)
mySet_1.add(2)
mySet_1.add(3)

mySet_2 = set()
mySet_2.add(4)
mySet_2.add(5)
mySet_2.add(6)
mySet_2.add(3)

union_set = mySet_1.union(mySet_2)
printSet(union_set, "Union of two sets")

intersection_set = mySet_1.intersection(mySet_2)
printSet(intersection_set, "Intersection of two sets")