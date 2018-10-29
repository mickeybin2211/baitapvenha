print ("""how many legs does a spider have ?
           1.none
           2.4 legs
           3.8 legs
           4.12 legs""")
while True :
    n=input ("your answer")
    if n.isdigit():
        numberN = int(n)
        if numberN == 1 or numberN ==2 or numberN==4:
            print ("wrong")
        elif numberN ==3:
            print ("correct")
            break
        elif numberN > 4:
            print("ABC")
           
    else :
        print ("your ans must be 1,2,3,4 enter again")