class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def showList(self):
        i=self.head
        while i !=None:
            print(i.data)
            i=i.next
    def addatEnd(self,data):

        # l.head=node(data)
        if self.head is None:
            o1 = node(data)


        i = self.head
        while i.next != None:
          i = i.next
        i.next=o1

    def addatpos(self,data,pos):
        o1 = node(data)
        i = self.head

        while i.next != pos:
            i = i.next
        i.next = o1

    def removeData(self,val):
        i = self.head
        while i != None:
            if i.data==val:
                i=i.next.next
                break
            else:
                i = i.next











l=LL()

l.addatEnd(2)
l.addatEnd(5)
l.addatEnd(7)
l.showList()
# l.addatpos(14,1)
l.removeData(2)
