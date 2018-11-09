class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        #新增节点的next，指向头节点
        #头节点只有一个"指针"，没有数据
        temp.setNext(self.head)
        #头节点指向新增节点
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        #从头节点开始遍历，需要判断如果头节点为None，为空，
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        #从头节点开始遍历，需要判断如果头节点为None，为空，
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        #需要两个“指针”，当前节点和前一个节点
        #previous落后于current，因此设置为None
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

if __name__ == '__main__':
    mylist = UnorderedList()

