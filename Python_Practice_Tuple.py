#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple",)  # create a Tuple with one item
print(type(thistuple))

#NOT a tuple
thistuple = ("apple") # one item considers default data type string
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")  # A tuple can contain different data types
print(tuple1)

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets tuple() method to make a Tuple
print(thistuple)
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])


y = list(thistuple) # Convert to list to add an Item
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry") # Add tuple to a tuple
y = ("orange",)
thistuple += y
print(thistuple)


y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# unpack Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# FOR Loop

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
for i in range(len(thistuple)):
  print(thistuple[i])

#While loop

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join and Multiply
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
