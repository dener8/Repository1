i=0
L=[]        
while True:
    a,b=input().split()
    a=int(a)
    b=int(b)
    L=L+[0]
    L[i]=a+b
    i+=1
    if a+b==0:
        break

i=0
while True:
    print(L[i])
    i+=1
    if L[i]==0:
        break
