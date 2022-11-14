# If is a key word / control flow
# In most programming lang we use { } curly bases to put a code but Python not need : and indentation (White space before the statement) to identify code
# If you want to understand a code in Python just go line by line
a=10
if a < 15 : # Returns true
    pass  # Dont act / do nothing
if a < 15:
    print("a is lesser than 15")

if 24 < 15:
    print("if loop ") # not going to execute as 24 < 15 is false
####################################
if 30 < 10 :
    print(" 30 lesser than 10")
else :
    print("if statement is wrong")
####################################
# Nested if , if you want to use multiple if conditions use elif keyword
income=int(input()) # input("enter salary ") # input always a takes as string to use like income=int(input())
if income < 50 :
    print("i will buy phone")
elif income < 70 :
    print("i will buy car")
elif income < 90 :
    print("i will buy house")
else :
    print("i will buy everything")

#################################### Discount program
Total_price = int(input())
if Total_price > 20000 :
    discount = Total_price * .20
    print("Discount will be ", discount)
elif Total_price <= 7000 :
    discount = Total_price * .05
    print ("Discount will be ", discount)
else:
    print ("wont be able to give any discount")

#######################################
coup = input() # input() mentod by default takes as string
if coup == "RANDAAS5" :
    print("you will be able to get discount of %5")
else:
    print("Kindly use a valid coup code")
#######################################

study_hr=int(input())
if study_hr < 1:
    print("It may take 8 to 10 months to transf")
elif study_hr < 4 and study_hr > 1 :
    print("it may take 6 months to tansfarm")
elif study_hr > 10:
    print("it will take 3 months to tranf")
else:
    print("it will be difficult to get a job")
######################################
s=input('enter insti name')
course=input('enter course name')
if s == 'oneneuron' :
    if course =='dsa':
        print("yes its available")
    elif course == 'blockchain':
        print("its not available , kindly raise a demand request")
    elif course == 'fsds':
        print("fsds is available as part of oneneuron")
    else:
        print("none of the courses available")
elif s =='oneplus':
    if course == 'c++':
        print("C++ course is available in oneplus")
    else:
        print("course is not available in oneplus")
else:
    print("enter a valid institute name")
########################################################
############
#
#
#                      FOR
#
#
#

l=[1,2,3,4,5,6,7]
print(l)
print(type(l))

for i in l:  # i local variable for for loop to store value temp
      print(i)

for i in 'venkat' :
    print(i)

l=[1,2.2,'Asdf',True,4+7j]
for i in l:
    print(type(i))
####################
l=[1,2,3,4,5,6,7]
l2=[]
for i in l:
    print(i+2)
    l2.append(i+2)
    print(l2)
##################  Get integers from the list
l=[2,45,78,12,"venkat",6+7j,[56,67,78]]
l1=[]
for i in l:
    if type(i) == int :
        l1.append(i)
        print(l1)
print(l1)
################## For else --- Only exists in Python
l=[2,45,78,12,"venkat",6+7j,[56,67,78]]
l1 = []
l2=[]
l3 = []
for i in l:
    l1.append((l.index(i))) # Print index of all the elements
   # print("index" , i , "for an element", l[i])
    if type(i) == str : # extract all str chars
        l2.append(i)
    elif type(i) == int:
        l3.append(i**2)  # Square of an int element
print(l1, l2, l3)
##############################  Display sum of even numbers from the list
numbers = [12, 75, 150, 180, 145, 525, 50]
n2=[]
for i in numbers :
    if i %2 ==0 :
        n2.append(i)
print(n2)

#############################
s='string'
for i in s :
    print(i)
else:  # If for loop is going to complete itself then it will come to else
    print("i am from else")

#######################
s='string'
for i in s :
    if i =='n':
        break
    print(i)
else:  # If for loop is going to complete itself then it will come to else
    print("i am from else")

#######################################
###
###
###    WHILE
###
###
#######################################
a=1
while a<6:    #always check weather its True / false ; if Its TRUE then it goes into loop
    print(a)
    a=a+1

########################
a=1
while a<5:
    print(a) # True prints a
    if a==4: # False so no break
        break
    a=a+1

########################
a=1
while a<5:
    print(a) # True prints a
    if a==3:# when 3==3 TRUE it triggers continue  .... Here it goes into infinite loop 1233333333
        continue # Directly takes to while loop without executing next line
    a=a+1

# correct answer for above program
a=1
while a<5:
    print(a) # True prints a
    a = a + 1
    if a==3:# when 3==3 TRUE it triggers continue  .... Here it goes into infinite loop 1233333333
        continue # Directly takes to while loop without executing next line

a=10
while a<5:
    pass
####################
#range(6) try to generate data except last / upperbound 0,1,2,3,4,5 / by default step size is 1
#range(0,6) # Starting from 0 to 6 ; 0,1,2,3,4,5
#list(range(3, 50, 2)) #3,5,7,9,11 till 50 ; here 2 is jump value/step value
print(list(range(3,10,-1))) #Output [ ] , going from 3 to 4 direction but jump has reverse direction so there is a conflict so output is blank
print(list(range(10,6,-1))) #[10, 9, 8, 7]   -5,-4,-3,-2,-1 0 1,2,3,4,5,6,7,8,9,10
print(list(range(10,-5,-2))) # [10, 8, 6, 4, 2, 0, -2, -4]

for i in range(7):
    print(i)

##############################  Pyramid print
n=5
for i in range (0,n):
    for j in range(0,i+1):
        print("*" , end="") # by default end value is \n , here it appends something at the end of value
    print("\r")

############################### Get indexes of values
t=(3,4,4,5,6,7,7,8)
for i in range(len(t)):
    print(i, t[i])

t=(3,4,4,5,6,7,7,8)
#print(t[::-1]) # print reverse direction
for i in range(len(t)-1 , 0 , -1): # OP: 8776544 ; no 3 because excludes upperbound
    print(t[i])

t=(3,4,4,5,6,7,7,8)
#print(t[::-1]) # print reverse direction
for i in range(len(t)-1 , -1 , -1): # OP: 87765443
    print(t[i])


t=(3,4,4,5,6,7,7,8)
#print(t[::-1]) # print reverse direction
for i in range(len(t)-1 , , -1): # Error not going to work
    print(t[i])

########################################
######
######
######   Dictionary key:value
######
#######################################3
d={'car':'toyota', 'year':2000}
print(d)
for i in d:
    print(i) # Gives keys
    print(i,d[i]) # gives key and value both

set={3,3,45,54,4545,5677,4343,232354,34343}
print(set) # provides unique set values unordered
for i in set:
    print(i)


