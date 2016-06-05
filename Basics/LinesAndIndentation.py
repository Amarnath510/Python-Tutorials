if True:
	print("True")
else:
	print("False")	

"""
Below code does not work because of the indentation issue.

if True:
	print("True")
else:
print("False")

"""	

"""
You can write multiple statements in a single line by using a semicolon. The only condition is no statement should start a new code block.
"""
import sys; x = 'foo'; sys.stdout.write(x)
