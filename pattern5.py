n=4
st=1
sp=n-1
for a in range(n):
    for b in range(sp):
        print(' ',end=' ')
    for c in range(st):
        print('*',end=' ')
    print()
    st+=2
    sp-=1
