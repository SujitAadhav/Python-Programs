"""
Create a dictionary and take input from the user and return the meaning
of the word from the dictionary
"""
print("Search the words to know their meaning...", end=" ")
d1 = input()
dic = {"set":"put, lay, or stand (something) in a specified place or position.",
       "mutable":"liable to change.",
       "immutable":"unchanging over time or unable to be changed.",
       "program":"a set of related measures or activities with a particular long-term aim."}
print(dic[d1])
