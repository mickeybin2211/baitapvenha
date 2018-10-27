n=int(input ("nhập n=?"))
if n<1:
    print ("kphai stn")
else:
    for i in range (2,n):
        if (n%i==0):
            print ("kphai")
            break    
    else :
        print ("snt")



