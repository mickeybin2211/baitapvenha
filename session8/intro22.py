list1=[]
while True :
    n=str (input  ( """tạo list :nhập thao tác muốn thực hiện ?
            C.create
            R.read
            U.update
            D.delete """ ))

    if n==str ("c") :
        a=input ("nhập thứ yêu thích của bạn ? ")
        list1.append(a)
    elif n==str("r"):
        if len(list1)==0:
            print ("danh sách rỗng ")
        else:    
            print (*list1,sep="\n")
    elif n==str ("u"):
        b = int(input ("nhập vị trí bạn muốn sửa"))
        d=input ("nhập thứ bạn muốn sửa")
        if b<=(len(list1)):
            list1[b-1]=(d)
        else :
            print ("vị trí sửa không hợp lệ  ")
    elif n==str ("d"):
        x=int (input ("nhập vị trí cần xoá "))
        if 0<x<(len(list1)):
            list1.pop(x)
        else:
            print ("vị trí xoá không hợp lệ")
 
    
