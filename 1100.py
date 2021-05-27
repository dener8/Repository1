a=input()
b=input()
c=input()
d=input()
e=input()
f=input()
g=input()
h=input()

white_first=list(a+c+e+g)
black_first=list(b+d+f+h)

answer=0

for i in range(0,64):
    if i%2==0:
        if white_first[i]=='F':
            answer=answer+1
    else:
        if black_first[i]=='F':
            answer=answer+1

print(answer)
