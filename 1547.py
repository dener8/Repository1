M=int(input())
L=[0,1,2,3]



for i in range(M):
    X,Y=input().split()
    X=int(X)
    Y=int(Y)

    L[0]=L[X]
    L[X]=L[Y]
    L[Y]=L[0]
    
print(L)




# 공이 사라져서 컵 밑에 없는 경우에는 -1을 출력한다.
