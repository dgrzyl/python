list1 = ["apple", "banana", "orange"]
list2 = ["banana", "orange"]

if set(list1).issubset(set(list2)):
    print("list1 zawiera się w list2")
else:
    print("list1 nie zawiera się w list2")