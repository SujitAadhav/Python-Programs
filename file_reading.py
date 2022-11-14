f = open("sujit.txt", "r")
# content = f.read()
# print(content)

# Reading 4 characters
# content = f.read(4)
# print(content)

# Reading next 4 characters
# content = f.read(4)
# print(content)

# This for loop reads line by line
# for line in f:
#     print(line)

# one function print one line
# print(f.readline())
# print(f.readline())
# print(f.readline())

# This function reads all lines from txt file
print(f.readlines())

f.close()