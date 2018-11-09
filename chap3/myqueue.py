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

if __name__ == '__main__':
    q = Queue()

    item = "hello"
    q.enqueue(item)
    item = 3
    q.enqueue(item)
    item = "world"
    q.enqueue(item)

