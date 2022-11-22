# When you create a project you see all directories / packages inside project folder. ex. .idea, pkg1
#creating a folder pkg1 , inside creating multiple files pkg1.py, pkg2 folder etc ..
#Collection of modules called a package / Each folder is a package with multiple modules
# project
#     pkg1
#         pkgtest1.py
#         pkgtest2.py
#     pkg2
#         pkgtest3.py
#

# What is the difference between modules and packages:
# In large companies they split code into modules and spread with in the team members.
# there will be a person who is going to integrate your .
# Package is a folder
# Module is a file

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
from pkg1 import pkgtest1 #OP: this is my function inside pkg1 test1 module
from pkg1 import pkgtest2
# OP:
# this is my function inside pkg1 test1 module
# this is my function inside pkg1 test2 module
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import my_module
course=my_module.get_course()
print(course)  #OP: ['data sciense', 'C', 'Python']
