# # # 1.Create a parent class Person with method name() returning:
# # # shiv 
# # # Create a child class Student with method course() returning:

# # class Person:
# #     def __init__(self,name):
# #         self.name=name
# #     def get(self):
# #         return self.name
# # class Student(Person):
# #     def __init__(self, name,course):
# #         super().__init__(name)
# #         self.course=course
# # s1=Student("shiv","Btech")
# # print(s1.get())
# # print(s1.course)

# # # 2.Create a parent class Vehicle with method start() returning:
# # # Vehicle Started
# # # Create a child class Car with method drive() returning:
# # # Driving Car
# # class Vehicle:
# #     def start(self):
# #         return "vehicle started"
    
# # class Car(Vehicle):
# #     def drive(self):
# #         return "driving car"
# # c1=Car()
# # print(c1.drive())
# # print(c1.start())
        
# # # 3.Create a parent class Animal with method sound().
# # # Create child classes Dog and Cat that override sound()
# # class Animal:
# #     def sound(self):
# #         pass
# # class Dog(Animal):
# #     def sound(self):
# #         print("bhow bhow")
# # class Cat(Animal):
# #     def sound(self):
# #         print("meow meow")
# # d=Dog()
# # d.sound()
# # c=Cat()
# # c.sound()

# # #  4: Shape Drawing
# # # Create a parent class Shape with method draw().
# # # Create child classes:
# # # Circle → "Drawing Circle" 
# # # Rectangle → "Drawing Rectangle

# # class Shape:
# #     def draw(self):
# #         pass
# # class Circle(Shape):
# #     def draw(self):
# #         print("Drawing Circle")
# # class Rectangle(Shape):
# #     def draw(self):
# #         print("Drawing Rectangle")


# # #  5: Login System
# # # Create a parent class Login with method authenticate().
# # # Create child classes:
# # # GoogleLogin → "Login with Google" 
# # # FacebookLogin → "Login with Facebook"

# # class Login:
# #     def authenticate(self):
# #         pass
# # class GoogleLogin(Login):
# #     def authenticate(self):
# #         print("Login with Google")
# # class FacebookLogin(Login):
# #     def authenticate(self):
# #         print("Login with Facebook")
        
# # g=GoogleLogin()
# # g.authenticate()
# # f=FacebookLogin()
# # f.authenticate()
    

# # # 6.   MULTILEVEL Inheritance :
# # # Create a Resume Builder using Multilevel Inheritance.
# # # Create a class Resume10th to store personal details and 10th academic details.
# # class personal_details:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# # class academics_details(personal_details):
# #     def __init__(self, name, age,marks):
# #         super().__init__(name, age)
# #         self.marks=marks
# # class Resume10th(academics_details):
# #     def __init__(self, name, age, marks):
# #         super().__init__(name, age, marks)
# #         print(self.name,self.age,self.marks)
# # r1=Resume10th("adarsh",12,49)
# #! Create a Calculator class with an add() method that can:
# #! Add 2 numbers
# #! Add 3 numbers
# #! Add 4 numbers
# class Calculator:
#     def add(self,a,b,c=None,d=None):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
        
#         sum = self.a+self.b
#         if c is not None:
#             sum+=self.c
#         if d is not None:
#             sum+=self.d
#         return sum

            
# a1 = Calculator()
# print(a1.add(1,2))
# print(a1.add(1,2,3))


# #! Question 2: Student Details (Method Overloading)
# #! Problem Statement
# #! Create a Student class with a display() method that can:
# #! Display only the student's name
# #! Display name and age
# #! Display name, age, and course
# class Student:
#     def display(self,name,age=None,course=None):
#         self.name=name
#         self.age=age
#         self.course=course
#         s=""
#         s+=name
#         if age is not None:
#             s+=","+str(age)
#         if course is not None:
#             s+=","+course
            
#         return s
# s1 =Student()
# print(s1.display("adarsh"))
# print(s1.display("adarsh",12))

# # Question 3: Area Calculation (Method Overloading)
# # Problem Statement
# # Create a class Area with a method calculate_area() that can:
# # Calculate the area of a square
# # Calculate the area of a rectangle
# # Calculate the area of a triangle

# class Area:
#     def display(self,length,width=None,height=None):
#         self.length=length
#         self.width=width
#         self.height=height
        
#         ans = length*length
        
#         if width is not None:
#             ans = length*width
#         if height is not None:
#             ans = length*width*height
            
#         return ans
# A=Area()
# print(A.display(2,4))
# # Question 1: Vehicle Example (Method Overriding)
# # Problem Statement
# # Create a parent class Vehicle with a method start_engine().
# # Create child classes:
# # Car
# # Bike
# # Override the start_engine() method in both child classes.
# # class Vehicle:
# #     def start_engine(self):
# #         pass
# # class Car(Vehicle):
# #     def start_engine(self):
# #         print("bike started")
# # class Bike(Vehicle):
# #     def start_engine(self):
# #         print("Car started")
# # V=Vehicle()
# # C=Car()
# # C.start_engine()

#! Question 2: Payment System (Abstraction)
#! Problem Statement
#! Create an abstract class Payment with an abstract method pay().
#! Create child classes:
#! CreditCard
#! UPI
#! NetBanking
#! Implement the pay() method in each child class.
class Payment:
    def pay(self):
        pass
class CreditCard(Payment):
    def pay(self):
        print("1 for credit card")
class UPI(Payment):
    def pay(self):
        print("2 for upi")
class NetBanking(Payment):
    def pay(self):
        print("3 for netbanking")