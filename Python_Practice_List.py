thislist = ["apple", "banana", "cherry"]
newlist = []
print(thislist)
print(type(thislist))
# Access the item
print(thislist[1]) # List is indexed , can be accessed through index number
print(thislist[-1]) # -ve indexed
print(thislist[0:2]) # range of index
print(thislist[0:])
print(thislist[:5])
print(thislist[0:10])
print(thislist[-3:-1])
if "apple" in thislist:
    print("yes , apple is in the list")

#Change the item
thislist[1] = "Fruit_changed"  # change the value , refere to the index
print(thislist)

thislist[1:3] = ["blackcurrant", "watermelon"] # Change reange of values
print(thislist)

thislist.insert(2, "InsertFruit") #INSERT value at index 2
print(thislist)

thislist.append("orange") #Append at the end of the list
print(thislist)

tropical=["mango", "pineapple", "papaya"] # extend , elements will be added at the end
thislist.extend(tropical)
print(thislist)

thislist.remove("apple") # Remove item
print(thislist)

thislist.pop() # Pop method removes by index , if nothing specified removes last item
print(thislist)
thislist.pop(1)
print(thislist)

# del thislist[0] # Deletes 0 index item
# print(thislist)
# thislist.clear() # clears or emptys the list
# print(thislist)
# del thislist # deletes entire list
# print(thislist)

#  FOR loop
for i in range(len(thislist)):  #Print all items by referring to their index number [0,1,2,3]
  print(thislist[i])

[print(x) for x in thislist]

# While Loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


for x in thislist:
  if "a" in x:
    newlist.append(x)
print(newlist)

thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)
thislist.reverse()
print(thislist)

mylist = thislist.copy()  #COPY  OR  mylist = list(thislist)
print(mylist)

