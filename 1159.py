num=int(input())
ll=[0]*26

for i in range(0,num):
    name=input()
    name=list(name)
    if name[0]=='a':
        ll[0]+=1
    elif name[0]=='b':
        ll[1]+=1
    elif name[0]=='c':
        ll[2]+=1
    elif name[0]=='d':
        ll[3]+=1
    elif name[0]=='e':
        ll[4]+=1
    elif name[0]=='f':
        ll[5]+=1
    elif name[0]=='g':
        ll[6]+=1
    elif name[0]=='h':
        ll[7]+=1
    elif name[0]=='i':
        ll[8]+=1
    elif name[0]=='j':
        ll[9]+=1
    elif name[0]=='k':
        ll[10]+=1
    elif name[0]=='l':
        ll[11]+=1
    elif name[0]=='m':
        ll[12]+=1
    elif name[0]=='n':
        ll[13]+=1
    elif name[0]=='o':
        ll[14]+=1
    elif name[0]=='p':
        ll[15]+=1
    elif name[0]=='q':
        ll[16]+=1
    elif name[0]=='r':
        ll[17]+=1
    elif name[0]=='s':
        ll[18]+=1
    elif name[0]=='t':
        ll[19]+=1
    elif name[0]=='u':
        ll[20]+=1
    elif name[0]=='v':
        ll[21]+=1
    elif name[0]=='w':
        ll[22]+=1
    elif name[0]=='x':
        ll[23]+=1
    elif name[0]=='y':
        ll[24]+=1
    else:
        ll[25]+=1

for i in range(0,26):
    if ll[i]>=5:
        print(ll[i])
        
    
