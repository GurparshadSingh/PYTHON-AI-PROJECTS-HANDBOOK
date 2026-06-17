# 🟢 1. Public (open access)
# 👉 No underscore
# class Student:
#     def __init__(self, name, marks):
#         self.name = name        # public
#         self.marks = marks          # public

# s = Student("Aman", 20)

# print(s.name)   # ✅ works
# print(s.marks)    # ✅ works
# 🧠 Meaning:

# Everything is freely accessible from outside.

# 🟡 2. Protected (convention only)
# 👉 Single underscore _x
# class Student:
#     def __init__(self, name, marks):
#         self._name = name       # protected
#         self._marks = marks

# s = Student("Aman", 20)

# print(s._name)   # ⚠️ works, but “don’t touch”
# print(s._marks)    # ⚠️ works, but not recommended
# 🧠 Meaning:
# “Internal use only”
# Still accessible, but developers agree not to touch it directly

# 👉 Think: “gentle warning label, not a lock”

# 🔴 3. Private (name mangling)
# 👉 Double underscore __x
# class Student:
#     def __init__(self, name, marks):
#         self.__name = name      # private
#         self.__marks = marks

#     def show(self):
#         return self.__name, self.__marks

# s = Student("Aman", 20)

# print(s.show())     # ✅ works (safe access)
# ❌ Direct access fails:
# print(s.__name)     # ❌ AttributeError
# 🕵️ But Python secretly stores it like:
# print(s._Student__name)  # ✅ works (name mangling)
# 🧠 Quick mental model
# Type	Syntax	Access	Meaning
# Public	x	Anywhere	Open door 🚪
# Protected	_x	Allowed but discourmarksd	Warning sign ⚠️
# Private	__x	Not directly accessible	Hidden name drawer 🗄️




# #! getters and setters 
# class Student:
#     def __init__(self,marks):
#         self.__marks=marks
    
#     def get(self):
#         return self.__marks
    
#     def set(self,marks):
#         if marks<0:
#             raise ValueError("marks cannot be negative")
#         self.__marks=marks

# s1= Student(12)
# # s1.__marks() #! not possible coz marks is protected just use getter and setter here to get set
# print(s1.get())
# # s1.set(-1)
# print(s1.get())





# #! cls it is a basically of a class not just of one object basically of whole building
# class Student:
#     marks=14
#     def __init__(self,marks):
#         self.marks=marks
    
#     # @classmethod
#     def print_marks(cls):
#         print(cls.marks)
        
# s1= Student("adrsh")
# s1.print_marks()#uses self
# Student.print_marks()#uses cls


        
# class Student:
#     def __init__(self,marks):
#         self.__marks=marks
#     @property
#     def marks(self):
#         return self.__marks
    
#     @marks.setter
#     def marks(self,value):
#         if value<0:
#             raise ValueError("marks cannot be negative")
#         self.__marks=value

# s1= Student(12)
# print(s1.marks) #property so call it like prop. not like a function






# class Student:
#     def __init__(self,marks):
#         self.__marks=marks
#     @property
#     def marks(self):
#         return self.__marks
#     @marks.setter
#     def marks(self,val):
#         if val<0:
#             raise ValueError("marks cant be negative")
#         self.__marks=val

        
# s1=Student(12)
# # print(s1.__marks)
# print(s1.marks)
# s1.marks=14
# print(s1.marks)



# class BankAcc:
#     def __init__(self,balance):
#         self.__balance=balance
#     @property
#     def balance(self):
#         return self.__balance
#     @balance.setter
#     def balance(self,bal):
#         if bal<0:
#             raise ValueError("balance cant be negative")
#         self.__balance=bal
        
# b1=BankAcc(1200)
# print(b1.balance)
# b1.balance=1100
# print(b1.balance)


# class BankAcc:
#     def __init__(self,balance):
#         self.__balance=balance
    
#     def print_bal(cls):
#         print(cls.__balance)

# b1=BankAcc(1200)
# b1.print_bal()


# from abc import ABC ,abstractmethod

# ek abstract class
# class Animal:
#         @abstractmethod
#         def sound(self):
#             pass
        
#         @abstractmethod 
#         def jumps(self):
#             pass
        
# class Dog(Animal):
#     def sound(self):
#             return "barks"
#     def jumps(self):
#             return "jumps"
# d=Dog()
# print(d.sound())

