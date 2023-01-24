from collections import Counter

s="you have two number and they have also two number"

s1=""
news=s.split(" ")
c=Counter(news)
list=[]
for key,val in c.items():
    if val==1:
        list.append(key)
for i in list:
    s1+=i

print(s1)