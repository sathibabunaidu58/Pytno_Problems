class DemoClass:
    num = 101

    def __init__(self, data):
        self.num = data

    def read_number(self):
        print(self.num)


obj = DemoClass(55)

obj.read_number()

obj2 = DemoClass(66)

obj2.read_number()