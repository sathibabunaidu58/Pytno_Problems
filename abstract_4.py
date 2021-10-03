

class Parent:

	
	def show(self):
		print("Inside Parent class")


class Child(Parent):
	
	
	def display(self):
		print("Inside Child class")

# Driver's code
obj = Child()
obj.display()


obj.show()
