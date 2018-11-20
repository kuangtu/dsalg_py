
def binarySearch(alist, item):
    start = 0
    end = len(alist) - 1
    found = False
    while start <= end and not found:
        mid = (end + start) // 2

        if alist[mid] == item:
            found = True
        else:
            if alist[mid] < item:
                start = mid + 1
            else:
                end = mid - 1

    return found

def binarySearch_Rec(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist)//2  #取整
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return binarySearch(alist[:mid], item)
            else:
                return binarySearch(alist[mid+1:], item)

if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))
    print(binarySearch_Rec(testlist, 3))
    print(binarySearch_Rec(testlist, 13))

