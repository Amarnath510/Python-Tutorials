"""
How to print integers side by side
"""

# DON'T FORGET TO IMPORT THIS IF YOU ARE USING 2.x. IN 3.x it is a built in function.
from __future__ import print_function
N = 10
for i in range(1, N + 1):
	print(i, end='') # this end indicates the gap that should be present between two integers in the output.

print("\n")

for i in range(1, N + 1):
	print(i, end=' ')

"""
How to read data from STDIN for Arrays, Names bla bla

Consider there are 3 records,
	3
	"amarnath" 10 20 30 
	"sushma" 40 50 60
	"prasad" 70 80 90

Now we should read them and display in python.

raw_input will give you the entire string and we need to parse it for our needs.
"""
"""
N = int(raw_input())

dictionary = {}

for i in range(0, N):
	# we will get the whole string
	# so we will split it by space. By default split is space
	total_str = raw_input().split() 
	name = total_str[0]

	total_marks = 0
	for index in range(1, len(total_str)):
		x = int(total_str[index])
		total_marks += x

	dictionary[name] = total_marks

print(dictionary)		
"""

"""
If you want to print the output side by side then?
We need to import print_function from future
"""