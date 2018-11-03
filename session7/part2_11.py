n= int (input ("nhập tháng ?"))
if n <=0 or n >12 :
    print ("số tháng phải lớn hơn 0 va nho hon 12")
elif n == 1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12: 
   print ("thang co 31 ngay")
elif n==2:
    print ("thang co 28 hoac 29 ngay")
else :
    print ("thang co 30 ngay")