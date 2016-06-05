"""
Classes and Objects.

What is self in the class methods?
You declare other class methods like normal functions with the exception that the first argument to each method is self. 
Python adds the self argument to the list for you; you do not need to include it when you call the methods
"""

class Employee:
	'common class for all employee'
	emp_count = 0

	' This is the constructor. This is called when a new instance of this class is created.'
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.emp_count += 1

	def displayCount(self):
		print(Employee.emp_count)
		return

	def displayEmployees(self):
		print "Name: " + self.name + ", Salary: " + str(self.salary)
		return

# NOTE: You don't need to add self here. self is like this in Java. Python will add it to your class methods.
emp1 = Employee('Amarnath', 10000)
emp2 = Employee('Sushma', 20000)

emp1.displayEmployees()
emp2.displayEmployees()
emp2.displayCount()

# We can Add or update or Delete attribute them at any time.
# Add attribute
emp1.age = 20 

# Update attribute
emp1.age = 15

# Delete attribute
del emp1.age

# We can check whether there is an attribute in the class or not
hasattr(emp1, "age") # returns true if age is an attribute in the class
getattr(emp1, "age") # returns value of age for emp1 object
setattr(emp1, "age", 10) # set value 10 to age for emp1
delattr(emp1, "age") # deletes the attribute age for emp1 object

