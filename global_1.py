# l = 10  # Global

# def function1(n):
    # l = 5 # Local
    # m = 8 # Local
#     global l
#     l = l + 8
#     print(n, "Hello", l)
#
# function1("Sujit")
# print(m)


x = 89
def sujit():
    x = 20
    def rohan():
        global x
        x = 88
    print("Before calling rohan()", x)
    rohan()
    print("After calling rohan()", x)

sujit()
print(x)