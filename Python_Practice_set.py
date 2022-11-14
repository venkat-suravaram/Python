thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))
print(type(thisset))

set1 = {"abc", 34, True, 40, "male"} # contains any data type
print(set1)

thisset = set(("apple", "banana", "cherry")) # using set() to make a set
print(thisset)


# for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Remove
thisset.remove("banana")
thisset.discard("banana")
x = thisset.pop()
print(x)
thisset.clear()
del thisset

# Join using union() , update()

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)