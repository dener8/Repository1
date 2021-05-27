

def answer(a,b,c):
    while True:
        a,b,c=input().split()
        b=int(b)
        c=int(c)


        

        if b>17 or c>=80:
           return Senior
        else:
            return Junior

        if a=='#' and b==0  and c==0:
            break


print(a\n)
print(answer(a,b,c))


