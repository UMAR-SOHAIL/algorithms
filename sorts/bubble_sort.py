# Created by Umar Sohail


def bubble_sort(unsorted_list):
     length = len(unsorted_list)
     for iteration in range(length):
         for item in range(1, length-iteration):
             if unsorted_list[-item] < unsorted_list[-item-1]:
                 unsorted_list[-item], unsorted_list[-item-1] = unsorted_list[-item-1], unsorted_list[-item]

     return unsorted_list
