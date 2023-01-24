from collections import Counter

s="vanshita"
l=[]
def checkchar(s):
    c=Counter(s)
    for key,val in c.items():
        if val >1:
            l.append(key)

checkchar(s)
print (l)