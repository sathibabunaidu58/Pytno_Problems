# define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj):
        self.name = name      # name(name of company) is public
        self._proj = proj     # proj(current project) is protected
    
    # public function to show the details
    def show(self):
        print("The code of the company is = ",self.ccode)

# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj):
        # calling parent class constructor
        Company.__init__(self, cName, proj)
        self.name = eName   # public member variable
        self.__sal = sal    ## define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj):
        self.name = name      # name(name of company) is public
        self._proj = proj     # proj(current project) is protected
    
    # public function to show the details
    def show(self):
        print("The code of the company is = ",self.ccode)

# define child class Emp
class Emp(Company):
    
    def __init__(self, eName, sal, cName, proj):
        
        Company.__init__(self, cName, proj)
        self.name = eName   # public member variable
        self.__sal = sal    # private member variable
    
    
    def show_sal(self):
        print("The salary of ",self.name," is ",self.__sal,)


c = Company("Stark Industries", "Mark 4")

e = Emp("Steve", 9999999, c.name, c._proj)

print("Welcome to ", c.name)
print("Here ", e.name," is working on ",e._proj)

e.show_sal()
    
    