class Student:
    def __init__(self, n, r):
        self.name = n
        self.roll = r
    def show(self):
        print("Name: ", self.name)
        print("Roll no.: ", self.roll)
s1 = Student('roses', 10)
s1.show()