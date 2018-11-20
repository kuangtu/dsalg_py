
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum%tablesize

class HashTable_Demo:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def put(self,key,data):
      #先确定一个hash值
      hashvalue = self.hashfunction(key,len(self.slots))

      #如果当前的slot没有元素，则放入key，对应的data列表中
      #放入data
      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        #如果输入的key，可以hash位置上面的key相同，则替换data值即可
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          #重新计算一个hash，原先(hash+1)%/size，
          #此时需要考虑找到下一个空slot，或者key相同的
          #就是有多个hash相同，已经填入了，此时比对的时候，
          #还需要检查一下key是否相同
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          #找到了空slot
          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            #key相同，替换data
            self.data[nextslot] = data #replace

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      #从slot开始进行遍历
      while self.slots[position] != None and  \
                           not found and not stop:
         #找到了slot上面的可以
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           #没有找到，后续一个个遍历，如果超过了之前的位置，
           #即：从startslot开始顺序查找，跳转到了头部继续查找
           #此时，不能再进行遍历了,停止
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data


    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size


if __name__ == '__main__':
    str = "test"
    res = hash(str, 10)
    print (res)
    H=HashTable_Demo()
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print(H.slots)
    print(H.data)

    print(H[20])

    print(H[17])
    H[20]='duck'
    print(H[20])
    print(H[99])
