a = 9
b = 8
# c = sum((a, b))     # Built in funtion
# print(c)

# def function1(a, b):
#     print("Hello you are in function 1: ", a+b)

def function2(a, b):
    """This is a function which will calculate an average of two numbers
    this function doesnt work for three numbers"""
    average = (a+b)/2
    return average

# v = function1(7, 5)
# print(v)

print(function2.__doc__)
x = function2(10, 2)
print(x)