f = open("sujit2.txt", "r")

# seek starts reading from mentioned character in this case it will start from 11th character
# tell shows the characters
print(f.tell())
f.seek(11)
print(f.readline())
print(f.tell())
print(f.readline())
f.close()
