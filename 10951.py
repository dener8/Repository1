i=0
L=[]
enter='\n'

while True:
    a,b=input().split()
    a=int(a)
    b=int(b)
    L=L+[0]
    L[i]=a+b
    i+=0
    if a==enter:   
        break
    
i=0
while True:
    print(L[i])
    i+=1
    if a==enter:
        break

