
class Class():
	def __init__(self, x):
		print(x)

class SubClass(Class):
	def __init__(self, x):

		super().__init__(x)


x = [1, 2, 3, 4, 5]
a = SubClass(x)
