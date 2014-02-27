class Person :
    def __init__(self, firstName = "unkown", lastName="" ) :
	    self._name = lastName + ", " + firstName

harry = Person("Harry", "Morgan")

print(harry._name)

p=Person()
print(p._name)