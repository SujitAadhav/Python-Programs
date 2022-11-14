# i=0
# while(True):
#     print(f"The value of i is: ", {i})
#     i=i+1
#     if(i>10):
#         # shop the loop
#         break;


# i=0
# while(True):
#     i=i+1
#     if(i==5):
#         continue
#     if(i>10):
#         break
#     print(f"The value of i is : {i}")


i=0
while(True):
    inp = int(input("Enter a number \n"))
    if inp > 100:
        print("Congrats you have entered a number greater than 100 \n")
        break
    else:
        print("Try again! \n")
        continue