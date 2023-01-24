from collections import Counter

ar1 = [ 20, 40, 80]
ar2 = [ 20, 80, 100]
ar3 = [ 80, 120]

commondic=[]
def check(ar1,ar2,ar3):
    c1=Counter(ar1)
    c2 = Counter(ar2)
    c3 = Counter(ar3)

    dic=dict(c1.items() & c2.items() & c3.items())
    for key,val in dic.items():
        for i in range(0,val):
            commondic.append(key)
    print(commondic)

check(ar1,ar2,ar3)

