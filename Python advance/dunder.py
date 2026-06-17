# Magic Dunder methods

#* 1>__init__(self,...)
# ?? can add more params with self 

# The __init__ method is the constructor of a class.
# It is called when a new object is created from the class.
# It’s used to initialize the object’s attributes.

# class Person:
#     def __init__(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
        
        
        
#*2>__str__(self,...)
# returns informal string representation better for users 
# class Person:
#     def __init__(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
    
#     def __str__(self):#no other params than self
#         return (f"the person with name{self.name} and age {self.age} is gamer")
# p1=Person("adarsh",16,"simbliwala")
# print(p1)


#*3>__repr__(self)
#more precise provides formal representation of strings better for developers and debugging
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def __repr__(self):
#         return(f"key = {self.x} ,val = {self.y}")
# p1=Point(1,4)
# print(p1)
        

#*4>__add__(self,other)
# The __add__ method allows the use of the + operator with objects of your class. 
# This is often used to define how two instances of a class interact when added together.

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def __add__(self,p):
#         return Point(self.x+p.x , self.y+p.y)
    
#     def __repr__(self):
        
#         return(f"key = {self.x} ,val = {self.y}")
    
# p1=Point(1,2)
# p2=Point(1,2)
# p=p1+p1
# print(p)

#*5>__len__(self)
# # using len(items)
# The __len__ method defines the behavior of the len() function for objects of your class.
# By implementing this method, you enable the ability to get the "length" or size of your custom object.
# class customList:
#     def __init__(self,items):
#         self.items=items
    
#     def __len__(self):
#         return len(self.items)
    
# list_=list((1,2,3,4))
# c1=customList(list_)
# print(len(c1))
# Here, __len__ is used to return the number of items in CustomList, making it compatible with len().

#*6>__getitem__(self,key)
# The __getitem__ method allows you to retrieve an item from an object using square brackets ([]), 
# similar to how lists and dictionaries work.
# class CustomDict:
#     def __init__(self,data):
#         self.data=data
    
#     def __getitem__(self,key):
#         return  self.data.get(key,"key not found")


# my_dict = CustomDict({"name": "Alice", "age": 30})

# print(my_dict["name"])


#*7> __eq__(self, other)
# The __eq__ method is used to define how equality is checked between two objects using the == operator.
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def __eq__(self,p):
#         return self.x==p.x and self.y==p.y
# point1 = Point(1, 2)
# point2 = Point(1, 2)
# point3 = Point(2, 3)

# print(point1==point2)
# print(point1==point3)


# In this example,
# the equality operator (==) is customized to compare Point objects based on their x and y coordinates.


#*8>__iter__(self)
# The __iter__ method allows an object to be iterated over in a for loop 
# or any context where an iterable is required. It should return an iterator object.





    