# class Student:
#     name = "Aditya" # class attributes
#     roll = 35

# studentA = Student()
# studentA.section = "K21BP"  # instance attributes
# studentA.name = "Dhanraj" # this will override the previous value. priority of instance attribute is higher compared to class attributes
# print(studentA.name, studentA.section)


# function definition in class
# class Student:
#     name = "Aditya"
#     roll = 35
    
#     # def getName():  this is wrong
#     #     print(name)
    
#     def getName(self):
#         print(self.name)
        
#     def greet(abc):  # we can write anything at the place of abc, it is just convention to write self
#         print("hello")
        
#     @staticmethod
#     def staticMethod(): # if we dont want to pass the whole object inside method then we need to make it to static method
#         print("This is static method")


# studentA = Student()

# Student.getName(studentA) # it is called like this
# studentA.getName()
# studentA.greet()
# studentA.staticMethod()


# constructer 
# class Student:
#     # @staticmethod  # after adding it there will be no argument passed implicitly by python, so self will be treated as explicit argument
#     def __init__(self, name,roll): # this is dunder method, whenever we will create an object this function will run
#         print("I am creating an object")
#         self.name = name
#         self.roll = roll


# student = Student("Aditya",36)
# print(f"Name of student is {student.name} and roll is {student.roll}")



# inheritence 

# simple inheritence
# class Shape:
#     name = ""
#     sides = None
    
#     def info(self):
#         print(f"Name of shape is {self.name} and number of sides are {self.sides}")
    

# class Rectangle(Shape):
#     name = "rectangle"
#     sides = 4
    
    
# rec = Rectangle().info()



# multilevel inheritence

# class A:
#     num1 = 1
    
# class B(A):
#     num2 = 2
    
# class C(B):
#     num3 = 3
    
    
# a = A()
# b = B()
# c = C()


# print(a.num1)  
# print(b.num1,b.num2)  
# print(c.num1,c.num2,c.num3)  


# multiple inheritence

# class A:
#     num = 1
    
#     @staticmethod
#     def show():
#         print("From A")
    
# class B:
#     num =2
    
#     @staticmethod
#     def show():
#         print("From B")
    
    
    
# class C(A,B): # which ever base class is passed first as the argument, value from that will be considered
#     pass


# c = C()

# print(c.num)

# c.show()



# # Use of super keyword

# class A:
#     def __init__(self) -> None:
#         print("From class A")


# class B:
#     def __init__(self) -> None:
#         print("From class B")
        
        
        
# class C(A,B):
#     def __init__(self) -> None:
#         super().__init__()


# c = C()



# class method

# class A:
#     num = 1 
#     @classmethod # now the value accessed by this function will be class attribute
#     def show(cls):
#         print(f"Value of F is {cls.num}")
        
        
# a = A()
# a.num = 45 # we have overidden the value of A but still after using the show method value will shown is equal to 1
# a.show()


# property method

# class A:
#     def __init__(self):
#         self._name = None

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value

# a = A()
# a.name = "Aditya Dhanraj"
# print(a.name,a._name)


# operator overloading (same as the below we can do for multiply divide and subtract etc)

class Number:
    def __init__(self,n) -> None:
        self.n =n
        
    def __add__(self,num):
        return self.n+ num.n
    def __str__(self) -> str: # same as toString() method of java
        return "This is number class"
        
        
n = Number(1)
m = Number(2)

print(n+m)
print(n) 