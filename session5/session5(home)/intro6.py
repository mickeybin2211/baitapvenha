a=int (input("nhap a"))
b= int (input ("nhap b"))
c= int (input ("nhap c"))
delta = b*b - 4*a*c
sqrt1 = (delta)**(1/2)
if a==0 and b==0 and c==0 :
    print ("vo so ng")
elif a==0 and b != 0 and c != 0:
    x3 = -c/b
    print ("nghiem duy nhat",x3)
elif delta <0 :
    print ("phương trình vô nghiệm")
elif delta == 0 :
    x = -b / (2*a)
    print ("ptrinh có nghiệm duy nhất =",x)
else :
    x1 = (-b+sqrt1)/(2*a)
    x2 = (-b-sqrt1)/(2*a)
    print ("2n0 là ",x1,x2)