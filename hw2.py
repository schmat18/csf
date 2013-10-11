# Name: ...
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

# ... write your code and comments here (and remove this line)
text = raw_input("Please input n: ")
n = int(text)
i=0
solution=0

while (i<=n):
    # solution = 3 +3 
    solution = (solution+(i))
    #print solution
    i=i+1
    
print solution

###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

# ... write your code and comments here (and remove this line)

for j in range(2,11):
    print (1/float(j))
    j=j+1  

###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

# ... write your code and comments here (and remove this line)
n = 10
triangular = 0
for i in range(1,n+1):
    triangular = triangular +i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2
###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

# ... write your code and comments here (and remove this line)

n=10
fact=1;
for i in range(1,11):
        fact=i*fact

print fact
###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

# ... write your code and comments here (and remove this line)
n=10
fact=1;
list=[]
for i in range(1,11):
        fact=i*fact
        list.append(fact)
for i in reversed(list):
    print i
###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

# ... write your code and comments here (and remove this line)
n=10
fact=1;
list=[]
answer = 1
for i in range(1,11):
        fact=i*fact
        list.append(float(fact))
for i in (list):
    answer= (1/i)
    
print answer
###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
#think Python
#stackoverflow.com
#wiki.python.org
###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
