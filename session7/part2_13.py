#Dựa vào chương trình đã tạo ở bài 1, tạo thêm một mục là “nhập lại mật khẩu” ô “mật khẩu” và ô “nhập lại mật khẩu” phải giống nhau, nếu khác nhau báo lỗi và bắt người dùng nhập lại.n = str (input ("ten dang nhap"))
while True:
    n = str (input ("ten dang nhap"))
    b= str (input ("nhap gmail"))
    c = str (input ("mat khau "))
    d=str (input ("nhap lai mat khau"))
    if  d==c:
        print("tao thanh cong")
        break
    else:
        print ("mat khau nhap lai khong trung khop")
