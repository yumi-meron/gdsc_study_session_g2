for i in range(2,51,2):
    if i%3==0 and i%5!=0:
        print("Three",end=" ")
    elif i%5==0 and i%3!=0:
        print("Five",end=" ")
    else:
        print(i,end= " ")
