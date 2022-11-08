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