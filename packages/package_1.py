class Addition:
	
	
	def __init__(self, f, s):
		self.first = f
		self.second = s
	
	def add(self):
		print('addition:- ',self.first+self.second)
		

	def sub(self):
		print('substrsction:- ',self.first-self.second)


	def div(self):
		print('division:- ',self.first/self.second)


	def mul(self):
		print('multiplicatin:- ',self.first-self.second)

obj = Addition(10, 20)


obj.add()
obj.sub()
obj.mul()
obj.div()



