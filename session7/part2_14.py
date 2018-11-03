while True:
    n = str (input ("ten dang nhap"))
    b= str (input ("nhap gmail"))
    c = str (input ("mat khau "))
    d=str (input ("nhap lai mat khau"))
    if  d==c:
        if "@gmail.com"  in b :
            if len(c)>=8:
                if c.isalpha() or c.isdigit():
                    print ("mkhau phai tren 8 ky tu va ca chu ca so")
                else :
                    print ("tao thanh cong ")
            else :
                print ("mkhau phai tren 8 ky tu va ca chu ca so")
            break
        else :
            print ("gmail khong hop le")
    
    else:
        print ("mat khau nhap lai khong trung khop")
