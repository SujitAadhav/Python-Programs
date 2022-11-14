# list1 = ["Sujit", "Ajit", "Sajit", "Arjit"]
# for item in list1:
#     print(item)

# list1 = [["Sujit", 1], ["Ajit", 4], ["Sajit", 98], ["Arjit", 32]]
# dict1 = dict(list1)
# for item, lollypop in dict1.items():
#     print(item, "and lollypop is ", lollypop)

# Quiz
# Check array numbers is numaric or not and print the numbers
# which is greater than 6
items = [int, float, "Sujit", 4,5,6,3,6,12,56,76,756,32,34,56,65]
for item in items:
    if str(item).isnumeric() and item > 6:
        print(item)