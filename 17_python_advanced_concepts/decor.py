# def decorator(func):
#     def wrapper():
#         print("firstly this will execute")
#         func()
#         print("i will execute after the function")
#     return wrapper

# @decorator
# def say_hello():
#     print("say hello function")

# say_hello()
    
    
def decorator(func):
    def wrapper(*args, **kwargs):
        print("before function this executes")
        result = func(*args, **kwargs)
        print("after function executes")
        
        return result
    return wrapper

@decorator
def add(a,b):
    print(f"sum is: {a+b}")
    return a+b

@decorator
def greet(name,msg="hi..."):
    print(f"this function greets {name} with {msg}")

# add(1,2)
greet(name='sunandi',msg="dafa ho")

#* *args
#* ➡️ collects ALL positional arguments into a tuple

# **kwargs
#* ➡️ collects ALL keyword arguments into a dictionary

#* So the function is not “choosing” one — it is collecting whatever is given.

        