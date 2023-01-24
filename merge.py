
def Merge(d1, d2):
	return(d1.update(d2))
d1 = {'a': 3, 'b': 3}
d2 = {'d': 2, 'c': 6}

Merge(d1, d2)
print(d1)
