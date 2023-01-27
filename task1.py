start=int(input("enter a starting range"))
end=int(input("enter a ending range"))
l=[]
sq=[]


for i in range(start,end+1):
    l.append(i)

for i in l:
    sq.append(i*i)


vi=[]
c=0

d1=dict(zip(l,sq))
for key,val in d1.items():
    print(key,val)


for i in range(0,3):
    if c<3:
        n=int(input("enter a num to get a square of that number"))
        if  n in d1.keys() and n  not in vi   :
            k=d1.get(n)
            print(k)
            vi.append(i)
            # print("jj")

        elif  n in vi:

            c += 1
            print(" you lost one chance")
            # break

        else:
            c+=1
            print(" you lost one chance")
    else:
        print("you lost all the chances")



