# f = open("sujit2.txt", "w")
# a = f.write("Sujit is a very good bay")
# print(a)
# f.close()

# f = open("sujit3.txt", "a")
# a = f.write("and he is a intelligent boy \n")
# print(a)
# f.close()

# Handle read and write both
f = open("sujit2.txt", "r+")
print(f.read())
f.write("thank you")

