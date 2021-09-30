class a:
    static='hello'
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
n = a('sathi')
print(n.static)