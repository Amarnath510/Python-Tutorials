class Parent:
	parentAttr = 100
	def __init__(self):
		print("Calling Parent Constructor")

	def parentMethod(self):
		print("Calling Parent Method")

	def setAttr(self, attr):
		Parent.parentAttr = attr

	def getAttr(self):
		print(Parent.parentAttr)


# Inroder to ingerit any class we will write them as below. If you want to inherit multiple classes then separate the classes with comma

class Child(Parent):
	def __init__(self):
		print("Calling Child Constructor")	

	def childMethod(self):
		print("Calling Child Method")

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200) # this method is not there in Child so we call the parent's method.
c.getAttr()	# this method is not there in Child so we call the parent's method.