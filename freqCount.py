l=[1,3,2,1,3,5]

f={}
def freq(l):
    for i in l:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    return f


print(freq(l))