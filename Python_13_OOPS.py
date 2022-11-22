# It's very difficult to handle large code in Enterprise level - Same logic you can write with OOPS or without.
# to create a structured modules to create task sub tasks
# Increase the re-usablility of the code Ex. Java , scala etc
# Class: Blue print CUP is a clasee , Milton cup is an object :
# Objects:


l=[1,2,3,4,5,6]
for i in l:
    print(i)
# 1
# 2
# 3
# 4
# 5
# 6
######################################################
#Create a class
class car :
    pass

####################
class car :
        # in a class , a very first variable you are going to create is a pointer ( called self )
        # pass variable through pointer to class.
        # constructor , helps to take my methods as inuts // pass data to the class
    def __init__(self,brand_name,fuel_type,body_type): # init method , Start with __ and end with __ is called inbuilt method ; def is callinf function
        self.brand_name = brand_name
        self.fuel_type = fuel_type
        self.body_type=body_type
    def desc_car(self):
        print(self.brand_name,self.fuel_type,self.body_type)
innova = car('toyota', 'petrol', 'suv')
nexon = car('tata', 'petrol', 'suv')
fortuner = car('toyota', 'desiel', 'suv')
innova.desc_car()# with the help of class variable you can access anything
    #OP: toyota petrol suv
nexon.desc_car()
fortuner.desc_car()
    # toyota petrol suv
    # tata petrol suv
    # toyota desiel suv
print(innova.brand_name) #OP: Toyota


################################################

class Employee:
    #constructor of a class
    # Mainly used for assignments of instance variables
    def __init__(self,name,salary):
        # instance variables or instance attributes
        self.emp_name=name
        self.emp_salary = salary
    # Method of a  class
    def displayemployeeinfo(self):
        print("Employee name : ",self.emp_name, " , Employee Salary : ",self.emp_salary)
    # to get a physical existance we need to create a object
emp1 = Employee('ram', 1000) # now it holds some memory , physical entity
emp2 = Employee('Ved',2000)

print(emp1.displayemployeeinfo())
print(emp1.emp_name)
print(emp2.displayemployeeinfo())

### Difference between Class Variable and Instance Variable


#################  class without arguments
class car:
        # constructor is not required when you don't pass arguments
    def test(venkat):  ## init is required only when you pass data  ; "venkat" is a first variable / pointer
        print("this is my first method in my car class")
x=car()
x.test()  #OP: this is my first method in my car class
print(type(x)) # OP: <class '__main__.car'>  // Variable of a class is an object

################################### Get list and display reverse order

class list_parser :
    def parcer(self, a):
        if type(a)== list :
            for i in a :
                print(i)
    def reverse_list(self,a):
        if type(a)==list:
            print(a[::-1])
c=list_parser()
c.parcer([2,3,4,5,6,7])
c.reverse_list([2,3,4,5,6,7])
############################

class list_parser :

    def __init__(self,l):  ## passed value once and performing all of the tasks
        self.l=l

    def parcer(self):
        if type(self.l)== list :
            for i in self.l :
                print(i)
    def reverse_list(self):
        if type(self.l)==list:
            print(self.l[::-1])
c=list_parser([2,3,4,5,6,7])
c.parcer()
c.reverse_list()
#########################
# Create a class for dictionary parsing
# 1. Write a function to give all the keys
# 2. Write a function to give all the values
# 3. throw an exception if the input is not a dict
# 4. take input and parse a key and value
# 5. insert a new key value pair .

class Dict_parser :

    def __init__(self,d):  ## passed value once and performing all of the tasks
        self.d=d

    def parcer_keys(self):
        try:
            if type(self.d)== dict :
                for x in self.d:  # Print all Key names
                    print(x)
        except:
            print("error found")

    def parcer_values(self):
        try:
            if type(self.d)== dict :
                for x in self.d:  # Print all values in dict
                    print(self.d[x])
        except:
            print("error found")

    def unwrap(self):
        try:
            if type(self.d)== dict :
                for x in self.d:
                    print(x, self.d[x])
        except:
            print("error found")

    def inser_dict(self):
        try:
            if type(self.d)== dict :
             pass
        except:
            print("error found")


c=Dict_parser({'brand': 'Ford', 'model': 'Mustang', 'year': 1964})
c.parcer_keys()
c.parcer_values()
c.inser_dict()
c.unwrap()

############################################## Method 2
class Dict_parser :

    def __init__(self,d):  ## passed value once and performing all of the tasks
        self.d=d

    def parcer_keys(self):
        try:
            if type(self.d)== dict :
                return list(self.d.keys())
        except:
            print("error found in Keys function")

    def parcer_values(self):
        try:
            if type(self.d)== dict :
                return list(self.d.values())
        except:
            print("error found in values function")

    def unwrap(self):
        try:
            if type(self.d)== dict :
                for x in self.d:
                    print(x, self.d[x])
        except:
            print("error found")

    def inser_dict(self,k,v):
        try:
            if type(self.d)== dict :
             self.d[k]=v
        except:
            print("error found")


c=Dict_parser({'brand': 'Ford', 'model': 'Mustang', 'year': 1964})
c.parcer_keys()
c.parcer_values()
c.inser_dict('year2', 2022)
c.unwrap()
