class Person():
    
    def __init__(self, run, walk, eat):
        self.run = run
        self.walk = walk
        self.eat = eat
	
    def display1(self):
        print("      Running      ")
        print("      Walking      ")
        print("      Eating       ")

# subclass for Male		
class Male(Person):
    
    def __init__(self, mal_name, mal_age, mal_address):
        self.name = mal_name
        self.age = mal_age
        self.address = mal_address
        Person.__init__(self, mal_name, mal_age,  mal_address)
	
    def display2(self):
        
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Address: ", self.address)
        Person.display1(self)
		
 # creating object of superclass
mal = Male("Ram", 27, "Ayodhya") 

mal.display2()


# subclass for Female		
class Female(Person):
    
    def __init__(self, fem_name, fem_age, fem_address):
        self.name = fem_name
        self.age = fem_age
        self.address = fem_address
        Person.__init__(self, fem_name, fem_age,  fem_address)
	
    def display3(self):
        
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Address: ", self.address)
        Person.display1(self)
		
 # creating object of superclass
fem = Female("Sita", 25, "Janakpur") 

fem.display3()
