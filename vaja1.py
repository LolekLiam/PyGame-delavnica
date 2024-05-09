def funk(a):
    b=0
    for i in range(1,a+1):
        if x%i==0:
            b+=1
    if b==2:
        print("Je praštevilo")
    else:
        print("Ni praštevilo")
x=int(input())
funk(x)
