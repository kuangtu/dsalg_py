
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   #必须有一个base case
   if n < base:
      return convertString[n]
   else:
        #一步步向base case逼近
        #算法能够调用自己
      return toStr(n//base,base) + convertString[n%base]

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


rStack = Stack()

def toStrStack(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        #base case
        if n < base:
            rStack.push(convertString[n])
        else:
            #求余，将余数压入到堆栈中
            rStack.push(convertString[n % base])
        #逐渐逼近base case
        n = n // base
    res = ""
    #将堆栈中的余数弹出
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res


if __name__ == '__main__':
    numList = [1, 3, 5, 7, 9]
    ret = listsum(numList)
    print(ret)
    print(toStr(1453,16))
