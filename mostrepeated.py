s='ENGINEERING'
d={}
count=1
for let in s:
    if let not in d:
        d[let]=1
    else:
        d[let]+=1
print(d)
h=max(d.values())
for k,v in d.items():
    if h==v:
        print(k)
