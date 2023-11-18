s='MADHU SUDHAN MARNENI'
d={}
for word in s.split():
    d[word]=len(word)
print(d)
h=max(d.values())
for k,v in d.items():
    if h==v:
        print(k)
    
