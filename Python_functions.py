#Why we need functions - reusability of code - need to perform a code multiple times
# def keyword to define function (Definition)
# default datatype of function "Nonetype"
#ex. len(), max(), min(),sum() , print() is a function
list=[1,2,3,4,5]
print("Max number :" , max(list))
print("Min number :" , min(list))
print("Sum number :" , sum(list))

# How do function works
# They may or may not take any input / output
def welcome_message(): # Ex of a function which doesn't take any inputs and doesn't return anything
    print("welcome learning python learning") # this won't display until you call function
welcome_message() # calling function

# Doesn't accept anything but return something
def welcome_message(): # Ex of a function which doesn't take any inputs and doesn't return anything
    #print("welcome learning python learning with return something") # this won't display until you call function
    return "message from return "  # returning something
# print(welcome_message()) # OR below method
result = welcome_message()
print("output : ",result)


# Example which accespts some parameter and results some value
num1=10
num2=15

def avg_of_2_numbers(a,b):
    print("a b values : ", a,b)
    avg_result = (a+b)/2
    return avg_result
    print("output: ", )
output=avg_of_2_numbers(num1,num2)
print("output: ",output)

# create a fun to caluculate fatorial of a num

def factorial(n):
    if n==0 or n==1:
        return 1
    result = 1
    for num in range(1,n+1):
        result = result*num

    return result
x=0
ans=factorial(x)
print("factorial of a number" ,x, " = ", ans)

# return multiple values from a function

a,b,c = 2,3,4
print(a,b,c)
##################
def test(n):
    sqr = n*n
    cube = n*n*n
    return sqr , cube
num=3
sqr_ans , cube_ans = test(num)
print(sqr_ans,cube_ans)

##########

def fun():
    pass

def fun():
    print("this is my function")

fun()

######### Hold output of a function
def fun():
    print("this is my function")
fun()

## test
def test():
    return "this is my function"
type(test())
print(test()+"venkat")

##
def test():
    return 4,3,"venkat",[1,2,3,4,5]
print(test())

##
def fun(a):
    n=[]
     if type(a) == list:
        for i in a:
            if type(i) ==int:
                n.append(i)
    return n
print(fun([12,34,21,34]))

##
def func(a,b):
    if type(a) ==list and type(b) ==list:
        return a.extend(b)+ "extended both the lists"
    else:
        return "either of your data is not a list"
print(func(2323,3333))

##
def fun(a,b,c,d,e):
    return a,b,c,d,e
print(fun(1,2,3,4,5))

##Find a lenth of a string without using len() / Take a string as input and return length

def length(a):
    print("type of a : ", type(a))
    if type(a) == str :
       print("length of a string :" , len(a))
length("string")

def length(str):
    count=0
    for i in str:
        count=count+1
    return count
print(length('string'))

## find the index of elements

def find_index(str):
     for i in str:
         a = []
         a=str.index(i)
         print("value :", i,"of index :",a)
find_index("string")

## Take input as dict and op as list
def dic_to_list(dic):
    if type(dic) == dict:

## Take function as input and returns output

def upper(str):
    return str.upper()
def lower(str):
    return str.lower()
def casechange(func):
    message=func("text goes here")
    print(message)
casechange(upper)
casechange(lower)

## take list as argument

def test(food):
    for i in food:
        print(i)
#food=["apple","orange","Banana"]
test(["apple","orange","Banana"])

# function that takes list and print index details
def test(food):
    for i in food:

        print("Idex of ", i, " is : ", food.index(i))
#food=["apple","orange","Banana"]
test(["apple","orange","Banana"])

## lIST ALL file names in a directory

import platform
print(platform.node()) # get computer name
print(platform.platform()) # computer platform details
print(platform.processor())
print(platform.python_version())
print(platform.uname())

## print date and time python function
from datetime import datetime
# datetime object containing current date and time
DateTime = datetime.now()
print("now =", DateTime)
# dd/mm/YY H:M:S
dt_string = DateTime.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)


