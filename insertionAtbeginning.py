from collections import OrderedDict

insertBegin=OrderedDict([('1','vanshi'),('2','xyz')])
insertBegin.update({'3':'abc'})
insertBegin.move_to_end('3',last=False)
print(insertBegin)