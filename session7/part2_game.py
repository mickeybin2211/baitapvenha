from random import randint 


while True :
    a = randint(0,100)
    b = randint (0,100)
    c = randint ((a+b)-2,(a+b)+2)
    print (a,"+",b,"=",c)
    print ("Dung hay Sai")
    dapan = str (input ("nhap dap an: "))
    d=a+b-c
    if d==0 :
        if dapan=="sai":
            print ("gameover")
            break
        
    else:
        if dapan=="dung":
            print ("gameover")
            break
        





   
        
