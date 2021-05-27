m = int(input())
loc = [1, 2, 3]

for i in range(m):
    
    x, y = input().split()
    x = int(x)
    y = int(y)
    
    #a = 0
    for i in range(3):
        if loc[i] == x:
            break
    
    #b = 0
    for j in range(3):
        if loc[j] == y:
            break
    loc[a] = y
    loc[b] = x
    
print(loc[0])


#for i와 for j 두개가 필요한가? 
