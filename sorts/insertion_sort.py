#created by Umar Sohail

def insertion_sort(ulist):
    length = len(ulist)
    for iteration in range(1, length):
        key = iteration
        while key > 0 and ulist[key -1] > ulist[key]:
            ulist[key], ulist[key-1] = ulist[key-1], ulist[key]
            key -= 1
    return ulist
