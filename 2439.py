num = int(input())

for i in range(num):

    for j in range(num):
        if i+j<num-1:
            print(' ',end='')

    for j in range(num):
        if i+j>=num-1:
            print('*',end='')

    print()
