
print('palindrome of CADAC')
s='CADAC'
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j])

print('print only palindormes in CADAC')
s='CADAC'
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if s[i:j]==s[i:j][::-1]:
            print(s[i:j])
