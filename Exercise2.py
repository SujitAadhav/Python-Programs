# Exercise 2 - Faulty Calculator
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56 + 9 = 77, 56/6 = 4
# Your program should take operator and the two numbers an input from the user
# and then return the result

print("Enter first number \n")
num1 = int(input())
print("Enter second number \n")
num2 = int(input())
print("So what you want?"+"+-/%*")
operator = input()

if num1 == 45 and num2 == 3 and operator == "*":
    print("555")
elif num1 == 56 and num2 == 9 and operator == "+":
    print("77")
elif num1 == 56 and num2 == 6 and operator == "/":
    print("4")
elif operator == "*":
    mul = num1 * num2
    print(mul)
elif operator == "+":
    add = num1 + num2
    print(add)
elif operator == "/":
    div = num1 / num2
    print(div)
elif operator == "%":
    modu = num1 % num2
    print(modu)
elif operator == "-":
    subs = num1 - num2
    print(subs)
else:
    print("Error! Please check your input")
