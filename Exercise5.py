# Health Management System
# 3 clients - Sujit, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

def take(k):
    if k==1:
        c=int(input("Enter 1 for exercise and 2 for food"))
        if(c==1):
            value=input("Type here\n")
            with open("sujit-ex.txt", "a") as op:
                op.write(str([str(getdate())])+": " + value + "\n")
            print("Successfully written")
        elif(c==2):
            value=input("Type here \n")
            with open("sujit-food.txt", "a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
    elif(k==2):
        c=int(input("Enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("Type here \n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(getdate())])+": " + value + "\n")
            print("Successfully written")
        elif(c==2):
            value = input("Type here \n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
    elif(k==3):
        c=int(input("Enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("Type here \n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
        elif(c==2):
            value = input("Type here \n")
            with open("hammad_food.txt", "a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
    else:
        print("Please enter valid input (1(sujit),2(rohan),3(hammad)")

def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("sujit-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("sujit_food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==2:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==3:
        c=int(input("Enter 1 for exersise and 2 for food"))
        if(c==1):
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter valid input (sujit,rohan, hammad")
print("Health Management System: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for sujit 2 for rohan 3 for hammad"))
    take(b)
else:
    b= int(input("Press 1 for sujit 2 for rohan 3 for hammad"))
    retrieve(b)




