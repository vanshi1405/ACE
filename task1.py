start=int(input("enter a starting range"))
end=int(input("enter a ending range"))
l=[i for i in range(start,end+1)]
d1={i:i*i for i in l}

vi=set()
c=0


# d1=dict(zip(l,sq))
# for key,val in d1.items():
#     print(key,val)


for i in range(0,3):
    if c<3:
        n=int(input(f"enter a num to get a square of that number and number is between {start} to {end} "))
        if  d1.get(n) and n  not in vi   :
            print(d1.get(n))
            vi.add(n)
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



