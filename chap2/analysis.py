import numpy as np

def find_min_1(numberlist):
    min = numberlist[0]
    number = len(numberlist)
    for i in numberlist:
        isSmallest = True
        for j in numberlist:
            #第一个循环，找到比i小的
            if i > j:
                isSmallest = False
        if isSmallest:
            min = i
    return min


def find_min_2(numberlist):
    min = numberlist[0]
    for i in numberlist:
        if (i < min):
            min = i
    return min


if __name__ == '__main__':
    numberlist = [1, 2, 4, 6, 7]
    # min = find_min_1(numberlist)
    min = find_min_2(numberlist)
    print("the min is:", min)
