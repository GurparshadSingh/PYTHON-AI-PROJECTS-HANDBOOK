# # #Specific errors
# # # while True:
# # #     try:
# # #         a = int(input("Enter a number: "))
# # #         b = int(input("Enter another number: "))
# # #         div = a/b
# # #         print("Division is: ", div)
        
        
# #         #! specific error handling handles error that we are expecting and 
# #         #! can handle it in a specific way
# #     #* except ValueError:
# #     #*     print("galt krdiya")
# #     #* except ZeroDivisionError:
# #     #*     print("Zero se divide nahi kr skte")
    
# #         #! generic error handling handles all the errors but we dont know which error is coming
# #         #! and we cant handle it in a specific way
# #     # except Exception as e:
# #     #     print("Error: ", e)
# #     # except :
# #     #     print("An error occurred")
# #         #! default exception handling is when we dont handle the error at all and
# #         #! it will show the error message to the user
# #         #! but it will not crash the program and it will continue to run
# #         #! but it is not recommended to use default exception handling because
# #         #! it handles literally all the errors and it can hide the errors and make it difficult to debug the code
# #         #! catches even the keybord interrupt and system exit and it can make it difficult to exit the program
# # #*be it any tyoe of error it will be handled by the generic error handling and 
# # #* it will print the error message to the user but it will not crash the program and it will continue to run


# # #* raise is used to raise an error manually and 
# # #* we can use it to raise a specific error when a certain condition is met
# # #*python wont complain here because -5 is valid integer in python but 
# # #* we can raise an error manually if we want to check for a certain condition and 
# # #* if that condition is not met then we can raise an error
# # #! age = -5
# # #! if age < 0:
# # #!     raise ValueError("Age cannot be negative")

# # #!raise with try example

# # # try: 
# # #     age = -5
# # #     if age<0:
# # #         raise ValueError("Age cannot be negative")
# # # except ValueError as e:
# # #     print("Error: ", e)



# # #safe division calculator
# # from multiprocessing.sharedctypes import Value


# # while True:
# #     try:
# #         a=int(input("Enter a number: "))
# #         b=int(input("Enter another number: "))
# #         if b == 0:
# #             raise ZeroDivisionError("Zero cannot be used as a divisor")
# #         div =a/b
# #         print("Division is: ", div)
# #     except ValueError:
# #         print("Please enter a valid number")
# #     except ZeroDivisionError:
# #         print("Zero cannot be used as a divisor")
        
# # #list element finder
# #     numbers = [1, 2, 3, 4, 5]
# #     try:
# #         index =int(input("Enter the index of the number you want to find: "))
# #         if index < 0 or index >= len(numbers):
# #             raise IndexError("Index out of range")
# #         print(f"The number at idx{index} is: {numbers[index]}")
# #     except ValueError:
# #         print("Please enter a valid number")
# #     # except IndexError:
# #     #     print("Index out of range")
    
# # #Bank withdrawl system
# #     balance = 1000
# #     try:
# #         amount= int(input("Enter your amount: "))
# #         balance -= amount
# #         print("Withdrawal successful")
# #         print("Remaining balance:", balance)
# #         if amount<0:
# #             raise ValueError("amount cant be negative")
# #         if amount>balance:
# #             raise Exception("Insufficient balance")
# #     except ValueError as e:
# #         print("Error: ", e)
# #     # except:
# #     #     print("An error occurred")
    
    
    
#! student management portal
try:
    name = str(input("Enter student's name"))
    age = int(input("Enter age"))
    marks = int(input("enter marks"))

    if age<0:
        raise ValueError("age cannot be negative")
    if marks>=100 or marks<=0:
        raise ValueError("out of range")

    students = {
    1: "Aman",
    2: "Rohit",
    3: "Simran"
    }
    user_id = int(input("enter id"))
    print(students[user_id])

    divisor = int(input("enter divisor"))
    div = marks/divisor
except ValueError:
    print("cant divide by zero")
except ZeroDivisionError:
    print("not possible")
except Exception as e:
    print("Error:",e)
except KeyError:
    print("Student not found")
finally:
    print("Program ended")
