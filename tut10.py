# Dictionary is nothing but key value pairs
d1 = {}
# print(type(d1))
d2 = {"Sujit":"Bhakari",
      "Rohan":"Panir",
      "SkillF":"Roti",
      "Shubham":{"B":"magic", "L":"roti", "D":"Pasta"}}
d2["Ankit"] = "Junk Food"
d2[420] = "Kebabs"
del d2[420]
print(d2["Shubham"]["B"])
d3 = d2.copy()
del d3["Sujit"]
print(d2)
print(d3)
d2.update({"Leena":"Toffee"})
print(d2.keys())
print(d2.items())