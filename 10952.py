a=[]
i=0

a=[0]*10           #임의설정. 무한대로 설정해야함 

while True:

    A,B = input().split()
    A = int(A)
    B = int(B)
    
    a[i]=A+B
    i += 1
    a=[0]*i
    
    if A + B == 0:    # A and B ==0 은 왜 안되지 ? 
        break


for j in a:
    print(j)





# list assignment index out of range



# a,b = int(input()).split()가 안되는 이유 한번만 더 여쭤보기
