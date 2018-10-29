while True :
    n = input ("nhập mật khẩu")
    if n.isalpha() or  n.isdigit():
        print ("mkhau phai có sô và chữ và trên 8 ktu")
    else :
        if len(n)<=8:
            print ("mkhau phai có sô và chữ và trên 8 ktu")
        else :
            print ("đúng mk")
            break 
