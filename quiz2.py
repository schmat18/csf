#from a module called lab2
#import a variable called n
#print one of the following things:
#  "greater than 50"
#  "less than 50"
#  "equal to 50"
# Based on the value of n

from lab2 import n

#I should not try to type cast to string when instantiating answer
answer=""

if(n>50):
  answer ="greater than 50"
  
elif(n<50):
  answer ="less than 50"
  
elif(n==50):
  answer ="equal to 50"
  
else:
  answer= "Error"
#forgot to add the print at the end
print answer