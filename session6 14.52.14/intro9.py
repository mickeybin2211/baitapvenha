while True :
    n = input ("nhập mật khẩu")
    if n.isalpha():
        print ("mkhau phai có sô và trên 8 ktu ca hoa ca thương ")
    else :
        if len(n)<=8:
            print ("mkhau phai có sô và trên 8 ktu ca hoa ca thuong ")
        else :
            if n.islower() or n.isupper():
                print ("mkhau phai có sô và trên 8 ktu ca hoa ca thương ")
            else:
                print ("đúng mk")
                break 
    