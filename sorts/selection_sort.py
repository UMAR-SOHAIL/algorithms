# created by Umar Sohail

def selection_sort(ulist):
    length = len(ulist)
    for iter in range(length):
        index = iter
        for j in range(iter+1, length):
            if ulist[j] > ulist[iter]:
                ulist[iter], ulist[j] = ulist[j], ulist[iter]
    print(ulist)
    return ulist


#this part is for test purposes

unorded = [3,2,1243,45,1,2,342,1,2,5,3,123,0, -1]
selection_sort(unorded)
