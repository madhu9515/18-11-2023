n=4

for a in range(n):
    for b in range(n):
        if a==0 or a==(n-1) or b==0 or b==(n-1):
            print('*',end=' ')
    print()
