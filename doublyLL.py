class snode():
    def __init__(self,data):
        self.data=data
        self.next=None


class dnode():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SL():
    def __init__(self):
        self.head=None

    def showList(self):
        i = self.head
        while i != None:
            print(i.data)
            i = i.next

    def addatEnd(self, data):
        o1 = snode(data)
        if self.head is None:
            self.head=o1

        else:
            i = self.head
            while i.next != None:
                i = i.next
            i.next = o1

class DL(SL):
    def __init__(self):
        super().__init__()

    def addatEnd(self,data):
        o1 = dnode(data)
        if self.head is None:
            self.head = o1
            o1.prev=None

        else:
            i = self.head
            while i.next != None:
                i = i.next
            temp=i.next
            i.next = o1
            o1.prev=temp

    def showlist(self):
        super().showList()






a=print(int(input("choose singly or doubly 1=singly 2=doubly")))

if a == 1:
    l1 = SL()
    for i in range(0,10):
        l1.addatEnd(i)
    l1.showList()
else:
    l2 = DL()
    for i in range(11, 20):
        l2.addatEnd(i)
    l2.showlist()







