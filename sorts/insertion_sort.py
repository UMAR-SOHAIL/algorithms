#created by Umar Sohail

def insertion_sort(ulist):
    length = len(ulist)
    for iteration in range(1, length):
        while iteration > 0 and ulist[iteration -1] > ulist[iteration]:
            ulist[iteration], ulist[iteration-1] = ulist[iteration-1], ulist[iteration]
            iteration -= 1
    return ulist
