t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    Ncnt=0
    Pcnt=0
    for i in a:
        if(i==-1):
            Ncnt+=1
        else:
            Pcnt+=1
    if(Ncnt>Pcnt):
        opr=Ncnt-Pcnt
        if(opr%2==0):
            opr=opr//2
        else:
            opr=(opr+1)//2
        if((Ncnt-opr)%2==1):
            opr+=1
        print(opr)
    elif(Ncnt%2==1):
        print(1)
    else:
        print(0);
