while True:
    from random import randint
    list25=["gfshdfh","s1414","dhghghf"]
    a=randint(0,2)
    b=list25[a]
    from random import shuffle
    c=list(b)
    shuffle(c)
    print(c)
    ans=str (input ("nhập đáp án"))
    if ans==b:
        print("correct")
    else :
        print("wrong")