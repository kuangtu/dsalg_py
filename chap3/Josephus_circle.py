class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def josephus_cirle(namelist, num):
    namequeue = Queue()
    for name in namelist:
        namequeue.enqueue(name)

    while namequeue.size() > 1:
        #将放入到队列中的元素移除，然后放到入队列
        for i in range(num):
            namequeue.enqueue(namequeue.dequeue())

        #到达计数的元素，直接删除
        namequeue.dequeue()

    return namequeue.dequeue()

def test():
    for i in range(10):
        print(i)

if __name__ == '__main__':
    print(josephus_cirle(["Bill","David","Susan","Jane","Kent","Brad"],7))

