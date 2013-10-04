# Name: Matthew schult
# Evergreen Login: schmat18
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

# ... write your code and comments here (and remove this line)
##Problem ax^2+bx+cx
##x2-5.86 x+ 8.5408
a=1
b=-5.86
c=8.5408

partOne=-b/(2*a)
partTwo=(math.sqrt((b**2)-(4*a*c)))/(2*a)

solution = (str(partOne)+"+-"+str(partTwo))
print solution
###
### Problem 2
###

print "Problem 2 solution follows:"

# ... write your code and comments here (and remove this line)

from hw1_test import *

letters =[a,b,c,d,e,f]

for index in range(len(letters)):
        print letters[index]

###
### Problem 3
###

print "Problem 3 solution follows:"

# ... write your code and comments here (and remove this line)

print "(("+str(letters[0])+" and "+str(letters[1])+") or (not "+str(letters[2])+") and not ("+str(letters[3])+" or "+str(letters[4])+" or "+str(letters[5])+"))" 

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
#Think python
#http://www.tutorialspoint.com/python/python_for_loop.htm

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
#This assignment didn't take me long at all, I have done programming classes already 
#but nothing in python. By taking the examples from think python and the tutorialspoint website
# I was able to quickly complete this assignment. I was planning on working on the optional problems
#but due to time constraints and deleting my programs twice I will make due with this.