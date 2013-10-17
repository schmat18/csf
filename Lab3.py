

output = [0,1]
n= int(raw_input("Input the value of n: "))
series= str(raw_input("Input the value of series [SUM, FIBONACCI]: "))
series = series.lower()
print
temp=0

if (series == 'fibonacci'):
    for i in range(1,n):
        temp= output[i]+output[i-1]
        output.append(temp)
        print str(output[1:])

    print ("The value of the "+str(n)+" is equal to "+ str(output[n]))
elif (series == "sum"):
    for i in range(1,n+1):
        temp=(temp+ (i*3))
        print str(temp)
    print ("The value of the "+str(n)+" is "+str(temp))
    
else:
    print "Invalid String!"
