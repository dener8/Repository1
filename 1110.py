n=int(input())

input_num=n

cycle=0

while True:

    if 0<=n<=9:
        n=str(n)
        n='0'+n
    
    cycle+=1

    n=str(n)
    n=n[1]+str((int(n[0])+int(n[1]))%10)
    n=int(n)

    if n==input_num:
        break

print(cycle)

