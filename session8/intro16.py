like3=["music","the winter","bun cha"]
like3.append("đường Hoàng Hoa Thám")
i=int (input ("nhập thứ tự cần sửa?"))
like3[i]=input("nhập gì đó ")
like3.pop(1)
if "lol" in like3:
    like3.remove("lol")
else:
    print("không có lol")
    print(*like3,sep=" ")