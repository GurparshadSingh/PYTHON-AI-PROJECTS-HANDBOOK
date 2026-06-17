# Q1
# Create a Laptop class.

# Attributes:

# brand
# ram
# storage

# Method:

# details() prints all information.
# l1 = Laptop("Dell",16,512)
# l1.details()

# class Laptop:
#     def __init__(self,brand,ram,storage):
#         self.brand = brand
#         self.ram = ram
#         self.storage=storage
#     def details(self):
#         print(f"Brand:{self.brand},Ram:{self.ram},Storage:{self.storage}")
# l1 = Laptop("Dell",16,512)
# l1.details()


# Q2

# Create a Car class.

# Attributes:

# color
# speed

# Create 3 objects and change the color of one object after creation.
# class Car:
#     def __init__(self,color,speed):
#         self.color = color
#         self.speed = speed
# c1=Car("red",100)
# c1.color="brown"
# print(c1.color)
# c2=Car("green",101)
# c3=Car("blue",102)


# Q3

# Create a Book class.

# Methods:

# borrow()
# return_book()

# Both should print messages.
# class Book:
#     def borrow(self):
#         print("Book borrowed")
#     def return_book(self):
#         print("Book returned")
# b=Book()
# b.borrow()
# b.return_book()

# Q4

# Create a class Student.

# Class variable:

# school = "CGC"

# Instance variables:

# name
# rollNo

# Create 3 students.

# Change school name using:

# Student.school = "CU"

# Print all students' school names.

# class Student:
#     school="CGC"
    
#     def __init__(self,name,rollNo):
#         self.name=name
#         self.rollNo=rollNo
# s1=Student("guru",12)
# # s2=Student()
# # s3=Student()
# Student.school="CU"
# print(s1.school)
    
    
# Q5

# Create class Employee.

# Class variable:

# employeeCount = 0

# Every time an object is created, increase count.

# Output:

# Total Employees: 3

# class Employee:
#     employeeCount = 1
#     def __init__(self):
#         Employee.employeeCount+=1
#         # print(self.employeeCount)
# print(Employee.employeeCount)
# e1 = Employee()
# print(Employee.employeeCount)
# e1 = Employee()
# print(Employee.employeeCount)

# Q6
# Create:

# Person

# Attributes:

# name
# age

# Method:

# introduce()
#     Create child:

# Student(Person)

# Extra attribute:

# rollNo

# Use super().

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
# class Student(Person):
#     def __init__(self, name, age,rollNo):
#         super().__init__(name, age)
#         self.rollNo = rollNo
#     def introduce(self):
#         print(self.name,self.age,self,self.rollNo)
# # p=Person()
# s=Student("adr",12,30)

# print(s.age,s.name,s.rollNo)


# Q7
# Create:
# Animal
# Method:
# eat()
# Create:
# Dog(Animal)
# Method:
# bark()
# Call both using Dog object.

# class Animal:
#     def eat(self):
#         print("animal")
# class Dog(Animal):
#     def bark(self):
#         print("bark")
# d=Dog()
# d.eat()
# d.bark()

#problem
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__()
    def introduce(self):
        
class Student(Person):
    total_students = 0
    def __init__(self,name,age,rollNo,marks,branch):
        super().__init__()
        self.name=name
        self.age=age
        self.rollNo=rollNo
        self.__marks=marks
        self.branch=branch
        def get_marks(self):
            return self.marks
        def set_marks(self,newMarks):
            self.marks=newMarks
        Student.total_students+=1
        
class Teacher(Person):
    def __init__(self):
        super().__init__()
class Sportscaptain(Person):
    def __init__(self):
        super().__init__()
class College(Person):
    def __init__(self):
        super().__init__()
        
class Collegecaptain(Student,Sportscaptain):
    def __init__(self):
        super().__init__()
        
class GraduateStudent(Student):
    def __init__(self):
        super().__init__()