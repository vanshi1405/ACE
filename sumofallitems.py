d1={'a':3,'b':1,'c':1,'d':1,'e':1,}

list=[]
ans=0
def add(d1):
    for i in d1.values():
        list.append(i)

    ans=sum(list)
    return ans
print(add(d1))
        