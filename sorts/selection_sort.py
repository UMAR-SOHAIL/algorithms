# created by Umar Sohail

def selection_sort(ulist):
    length = len(ulist)
    for iter in range(length):
        for j in range(iter+1, length):
            if ulist[j] < ulist[iter]:
                ulist[iter], ulist[j] = ulist[j], ulist[iter]
    return ulist
