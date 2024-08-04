# # Immutual & Mutual

# #Immutual => once you define it You CANNOT Change it!
# str
# int
# float
# bool
# bytes
# tuple

# #Mutual => once you define it You CAN Change/ Modify it!
# list
# set
# dict

# #ex
# x = (1, 2) #tuple

# x[0] = 1  #get on error bc 'tuple' object does not support item assigment

# #ex
# z = (3, 4 )
# w = z

# z = (4, 5, 6)
# print(z, w) # doesn't affect it bc when you use immutual and you reassigning a new value for z(immutual)

# #ex => dict datatype and doesn't affect instead e takes the value of d and then d modify the index 0
# d = [8, 9]
# e = d
# d[0] = 100
# print(d, e)

# def get_largest_numbers(numbers, n):
#     numbers.sort()
    
#     return numbers[-n:]

# nums = [2, 3, 4, 1, 35, 125, 341, 9]
# print(nums)
# largest = get_largest_numbers(nums, 2)
# print(nums)

#In order to Want or Not your code to be modify use the Mutual and Immutual datatypes properly spefically for what you need
 
 
# !! List Comprehensions!!
x = [i for i in range(10)]  # for loop inside of a list
print(x)  # 0-9


x = [[j for j in range(5)]for i in range(10)]  # for loop inside of a array
print(x) # random differnt 10 list

x= [i for i in range(10) if i % 2 == 0] # even values or zero inside of this list
print(x)

# Argument in parameter types !!
def complicated_function(x, y):  # x,y=> parameters
     print(x,y) 
     pass

complicated_function(y = 2, x =1)

def complicated_function(x, y, z):
     print(x,y) 
     pass

complicated_function(1, z = 2, y = 3) # values=.arguments

def complicated_function(x, y, z = None): # optional argument => not required to pass it
     print(x,y) 
     pass

complicated_function(1, z = 2, y = 3)

def complicated_function(x, y, z = 10): 
     print(x, y, z)
     pass

complicated_function(1, 3) # default value for z if you don't call that parameter


# *args
def complicated_function(x, y, *args) :
     print(x, y, args)
     pass
complicated_function(1, 3, 2, 6, 8, 9, 1)

def complicated_function(*args) :
     print(args)
     pass
complicated_function(1, 3, 2, 6, 8, 9, 1)

def complicated_function(*args) :
     print(args)
     pass
complicated_function()

# *args **kwargs

def complicated_function(*args, **kwargs) : # accept any number of keyword argument
     print(args, kwargs)
     pass
complicated_function(x = 1, s = "hello", b = True) # stored inside of a dictionary

def complicated_function(*args, **kwargs) : 
     print(args, kwargs["s"])
     pass
complicated_function(x = 1, s = "hello", b = True)

def complicated_function(*args, **kwargs) : 
     print(args, kwargs["s"])
     pass
complicated_function(1, 2, 3, x = 1, s = "hello", b = True)


def complicated_function(a, b, c = True, d= False ) : 
     print(a, b)
     pass
complicated_function(*[1, 2], **{"c": "Hello", "d" : "cutie"}) # the ** will break this dictionary into its keyword arguments and pass that to the function

def complicated_function(a, b, c = True, d= False ) : 
     print(a, b, c, d)
     pass
complicated_function(*[1, 2], **{"c": "Hello", "d" : "cutie"})

#Glabal Interpreter Lock => can only have one thread in execution at a time!