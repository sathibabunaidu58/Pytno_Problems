class a:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.Code='Python'
    def display(self):
        print(self.name,self.age)
    def Language(self):
        print(self.Code)
class b(a):
    def number(self,ph):
        self.ph=ph
      
    def creat(self):
        super().display()
    def Language(self):
        return super().Language()
class c(b):
    def fee(self,money):
        self.money=money
    def Language(self):
        return super().Language()
n=a('sathi babu',23)
n.display()
n.Language()
m=b('sathi',25)
m.number(8096890143)
m.creat()
m.Language()
l=c('sathi',25)
l.Language()