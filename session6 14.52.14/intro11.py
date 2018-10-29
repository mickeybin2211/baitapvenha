loop = True
while loop :
    n=str  (input ("nhập n"))
    if n.isdigit():
        a = len (n)
        print ("số các số là ",a)
        loop = False
    else :
        print ("n phải là số")