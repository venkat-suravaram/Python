#space removal , Right and left
a=" venkat is great "
print(a.rstrip())
print(a.lstrip())
print(a.strip())

print(a.replace("v","xyz")) # Replace V with xyz , if v is not there it will not replace
print("venkat\tSuravaram".expandtabs()) # Remove tab space in the string
a="venkat"
print(a.center(40 , 't')) # tttttttttttttttttvenkatttttttttttttttttt // reserves 40 chars and places name in middle
print(a.isupper()) # False
print(a.islower())  #True
print(a.isspace()) #False
print(a.isdigit()) #checks if it has numbers // False
print(a.endswith('t')) #True
print(a.startswith('a')) #False


# variables and assignments
a = 30
b = 'name'
float_money = 100.50

print(a)
print(b)
print(float_money)

ram, sita = 10, 20
x = y = z = 10
print(x, y, z)
print(ram, sita)

# Global variable example
gvar = "from global"
def myfunc():
    print("i am from " + gvar)
myfunc()
print("i am out side myfun " + gvar)

#Example global and local variable declaration
# global key use variable anyplace
var1="Global variable"
def fun():
    global var3
    var3="use me with gloval key"
    var2 = "local variable"
    print("inside function" + var2)
    print(var3)
fun()
print(" I am outside function" +var1)
print("I am outside function" + var3)

#Get type of a data type

a= 100.50
print(a ,"type is ", type(a))


#type casting
int_var = 10
cast_float_var = float(int_var)
cast_string_var = str(int_var)
print(int_var , type(int_var))
print(cast_float_var , type(cast_float_var))
print(cast_string_var , type(cast_string_var))

# Boolean represent True / False
a=200
b=50
if(a<b):
    print("A<B")
else:
    print("A>B")


################## Strings
a='Hello World'
print(a)
print(a[0])
print(len(a)) # find length of string
#loop through string
for x in a:
    print(x)

#slicing
b = "Hello, World!"
print(b[2:5]) #Get the characters from position 2 to position 5
print(b[:5]) # Start to 5 // O/P: Hello
print(b[2:]) # Position 2 to end  //llo, world
print(b[-5:-2]) # From: "o" in "World!" (position -5) To, but not included: "d" in "World!"  (position -2):  // O/P: orl

## String modify
a = "  Hello, World!  "
print(a.upper())
print(a.lower())
print(a.strip()) #Removes whitespaces
print(a.lstrip())
print(a.rstrip())
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']

print("venkat\tSuravaram".expandtabs())  # Removetabspaceinthestring
print(a.center(40, 't'))  # tttttttttttttttttvenkatttttttttttttttttt//reserves40charsandplacesnameinmiddle
print(a.isupper())  # False
print(a.islower())  # True
print(a.isspace())  # False
print(a.isdigit())  # checksifithasnumbers//False
print(a.endswith('t'))  # True
print(a.startswith('a'))  # False


############### Operators
x = 5
y = 3

print("Addition of x + y = ", x + y)
print("Substraction of x - y = ", x - y)
print("Multiplication of x * y = ", x * y)
print("Float Division of x / y = ", x / y)
print("Integer Divison of x // y = ", x // y)
print("Modulus of x % y = ", x % y)
print("Power of y on x i.e; x ** y = ", x ** y)

# concat operation for string
str_data = "Jonny"
full_name = str_data + " " + "lee"
print("Full name = ", full_name)

# if we can use - as well ? IT will not work
# minus_str = "Jonny" - "Lee"
# print("Minus str = ", minus_str)

# multiply_str = "Jonny"*"Lee"
# print("Multiply str = ", multiply_str)

# power_str = "Jonny"**"Lee"
# print("Power str = ", power_str)

# power_str = "Jonny" ** 3
# print("Power str = ", power_str)

multiply_numeric_str = "Jonny" * 5
print("Multiply numeric str = ", multiply_numeric_str)

## Comparision operator
a = 10
b = 5
print("Result of a==b,", a == b)
print("Result of a!=b,", a != b)
print("Result of a>b,", a > b)
print("Result of a<b,", a < b)
print("Result of a>=b,", a >= b)
print("Result of a<=b,", a <= b)


## Logical  operator
m=10
n=8
print("m>10 and n<10 Result",m>10 and n<10)#FalseandTrue->False
print("m>20 or n<10 Result",m>10 or n<10)#FalseorTrue->
print("not(m>20 and n<10)Result",not(m>10 and n<10))
#not(FalseandTrue)->not(False)->True


####################  IF
a = 33
b = 200
if b > a:
    print("b is greater than a")


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


if a > b: print("a is greater than b") # Short hand IF
a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


######### While
i=1
while i<4:
    print(i)
    i=i+1

i=1
while i<4:
    print(i)
    if i==3:
        break
    i=i+1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


###############################  FOR
for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break



Age=int(input("Enter Age:"))
if Age >=18:
    print("I can vote")
elif Age < 18:
    print("It is a odd number")

x,y,z = input(),input(),input()
print(max(x,y,z))


##############
############
############
############
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

# Write a program to print revers 10 to 1
for num in range(10,0,-1):
    print(num)

thislist = [1, 2, 7, "Shashank", [6, 5, 4], "string"]
thislist2=[20,30,40]
print(len(thislist))
thislist.append(thislist2)
thislist.extend(thislist2)
#print("output of append: ", thislist)
print("output of extend: ", thislist)


