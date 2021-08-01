class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

    def Name(self):
        return self.firstname + ", " + self.staffnumber

p1 = Person("Mike","Beaumier")
print (p1.Name())

e1 = Employee(first="Mike",staffnum="Machine Learning Engineer",last="Beaumier")
print (e1.Name())
