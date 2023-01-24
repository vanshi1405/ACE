d1 = {'no' : [1, 2, 3],
            'name' : ['vanshi', 'kashvi', 'abs']}

x=list(d1.values())
d2=dict()
k=x[0]
v=x[1]
for i in range(0,len(x)+1):
    d2[k[i]]=v[i]

print(d2)