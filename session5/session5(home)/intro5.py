user_name = str (input ("ten dang nhap"))
password = str (input ("password"))
if user_name != "techkids" :
    print ("you a not user")
if user_name == "techkids":
    if password != "codethechange":
        print ("invalidpassword")
    else :
        print ("welcome")
