from collections import Counter

d1=[
    'vanshi','v','k','k']

def maxVote(d1):
    c=Counter(d1)
    #print(c)
    maxval=max(c.values())
    for i in c.keys():
        if c[i]==maxval:
            return c[i]



print(maxVote(d1))
