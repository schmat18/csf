# Name: Matthew Schult
# Evergreen Login: Schmat18
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

# ... write your code and comments here (and remove this line)
output=0
for x in range(1,100):
    output=(output + (x+5))
   
print output

###
### Problem 4
###


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

# ... write your code and comments here (and remove this line)


def divide(a,b):
    if b is not 0:
        return float(a)/float(b)
    else:
        return "FAIL: Divide by Zero Error"

print divide(10,2)
print divide(57,0)
print divide(26,-4)

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

# ... write your code and comments here (and remove this line)
myWords=['one','two','three','four','five','six','seven','eight','nine','ten']
myList = range(1,9)
for number in myList:
    if number % 2 ==0:
        myList[number-1] = myWords[number-1]

print myList

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

# ... write your code and comments here (and remove this line)

x = 0
for i in range(5):
  x = i
  y = divide(4*x,x**2) 

print y 


###
### Problem 7
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

# ... write your code and comments here (and remove this line)
output = {}
i=0
length = len(myList)
while(i<length):
    if i % 2 ==1:
        output[myList[i]]="even"
    else:
        output[myList[i]]="odd"
        
    i=i+1
        
print output
###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").