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







l=LL()
l.head=node(4)

l.addatEnd(2)
l.addatEnd(5)
l.addatEnd(7)
# l.addatpos(14,1)
l.showList()