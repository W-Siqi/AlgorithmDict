```py
class Employee:
    # public 
    empCount = 0  
    # private attribute
    __salary = 0
    # protected attribute
    _id = 'id'

    @staticmethod
    def staticMethod:
        pass
        
    # constructor
   def __init__(self, name, salary):
      self.name = name
      self.__salary = salary
      # STATIC member , if in this way
      Employee.empCount += 1
      # belong to object, if in this way
      self.empCount = 0

   # member function, is first argument ALWAYS be the 'self pointer' 
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.__salary

# instantiate 
e = Employee("Jack",66666)

# we can add/remove attribute dynamically!
# from this point, obejct is just like a dictionary
e.age = 6
del e.age


# some basic attributes of a object
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
```

```py
# inheritance
class Programmer(Employee): 
    # "overwrite"
    def displayEmployee(self):
        print "Im a programmer!"
        print "Name : ", self.name,  ", Salary: ", self.__salary
```