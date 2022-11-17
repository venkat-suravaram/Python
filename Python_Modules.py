# Modules are pre-designed code to use
#C:\Users\vsura\PycharmProjects\pythonProject\Python
#Some one has written all in-built functions for you. like list() mehtods , inside list there are sub methods

# you can find already existing functions here https://github.com/python/cpython/blob/3.10/Lib/os.py
## **** TestModule.py   Write your code / function / module in your file and save as .py in same directory
# def testadd(a,b):
#     return a+b
#
# def testmul(a,b):
#     return a*b
#
# def testsub(a,b):
#     return a-b

import os
print(os.getcwd())
#C:\Users\vsura\PycharmProjects\pythonProject\Python

#############################
import TestModule
TestModule.testmul(10,20)
print(TestModule.testmul(10,20))

TestModule.testadd(1,5)
print(TestModule.testadd(1,5))

##############################
# if you would like to import only 1 function from all inside

import TestModule
from TestModule import testmul
print("Imported only required function from module: ",testmul(1,5)) #Imported only required function from module:  5

################################
# When you don't know what all the functions in the module then you could do this.
import TestModule
from TestModule import *
print("Imported only required function from module: ",testmul(1,5))
print("from TestMod import * : ",testsub(10,5))

###############################
#open("my_module.py",'w')
# Created Moduled and function inside , resuing multiple times
# data={"name":"ssj institute","course":["data sciense","C","Python"], "Greeting":"Greetings from ssj institute"}
# def get_course():
#     return data["course"]
# def get_greetings():
#     return data["Greeting"]
import my_module
my_module.get_course()
print("my_module.get_course() : ---  ",my_module.get_course())
print("my_module.greetings()  :---   ",my_module.get_greetings())

###############################
