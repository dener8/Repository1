H,M=int(input()).split()


if H==0 and 0<=M<=44:
    print('23',M+15)

elif 0<=H<=23 and 0<=M<=59:
    T=(H*60)+M
    H=(T-45)//60
    M=(T-45)%60
    print(H,M)



#시간 따로따로하는거 맞으려나 
