class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def testStack():
    s = Stack()
    print(s.isEmpty())
    s.push('a')
    print(s.size())

def revString(str1):
    s1 = Stack()
    strlist = [ c for c in str1]
    for c in strlist:
        s1.push(c)

    revlist = []
    while not s1.isEmpty():
        revlist.append(s1.pop())

    return "".join(revlist)




if __name__ == '__main__':
    str1 = "apple"
    # testStack()
    revstr = revString(str1)
    print(revstr)