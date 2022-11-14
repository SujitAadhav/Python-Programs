# Lambda functions or anonymous functions
# def add(a, b):
#     return a + b

# This is lambda function
# add = lambda a, b : a + b
# print(add(5, 7))

minus = lambda x, y : x - y
print(minus(12, 2))

# Other programmers can use lambda functions like this
a =[[1, 14], [5, 6], [8,23]]
a.sort(key=lambda x:x[1])
print(a)