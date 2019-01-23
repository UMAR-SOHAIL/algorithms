# Created by Umar Sohail

def bubble_sort(unsorted_list):
     length = len(unsorted_list)
     for iteration in range(length):
         for item in range(1, length-iteration):
             if unsorted_list[-item] < unsorted_list[-item-1]:
                 unsorted_list[-item], unsorted_list[-item-1] = unsorted_list[-item-1], unsorted_list[-item]
            
                 
            
            
            
            
            
        


# for test purposes only
a = [3,6,32,1,3,1,3435,6547,34,234,64,5758,769,789,790,890,678,567,456,234,346,47,35,2,3452,45,2,43654,7567]
print(a)
bubble_sort(a)
print(a)
