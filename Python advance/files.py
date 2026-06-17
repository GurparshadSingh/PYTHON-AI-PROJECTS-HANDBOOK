#*This code demonstrates how to create an iterator from a 
#! list and retrieve the next element using the `next()` function.
# nums = [1, 2, 3, 4, 5]
# it=iter(nums)
# print(next(it))
# #* its just like using a pointer at index 0 then next()will moves the pointer to index 1 
# # and so on until the end of the list is reached.

# #* generator
# def count_to_n(n):
#     for i in range(1, n + 1):
#         yield i
# for number in count_to_n(5):
#     print(number)
#* The `yield` statement allows the function to return a value and pause its execution, 
#* resuming from the same point when the next value is requested. 
#* This makes it memory efficient, 
#* as it generates values on-the-fly rather than storing them all in memory at once.


# nums = [1, 2, 3, 4, 5]
# odds = filter(lambda x: x % 2 != 0, nums)
# odds = list(filter(lambda x: x % 2 != 0, nums))
# # odds = list(map(lambda x: x * 2, odds))
# print(odds)
# add= lambda x, y: x + y
# print(add(3, 5))

class Name:
    def get_name(self,name):
        return name


class Age:
    def get_age(self,age):
        return age


class Details(Name, Age):
    def get_details(self,name,age):
        return self.get_name(name), self.get_age(age)


obj = Details()
print(obj.get_details("Gurparshad", 21))
