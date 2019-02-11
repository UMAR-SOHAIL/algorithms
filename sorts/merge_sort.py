#created by Umar Sohail

def merge_sort(ulist):
    length = len(ulist)
    if length > 1:
        division = length // 2
        first_half = ulist[:division]
        second_half = ulist[division:]
        length_first_half = len(first_half)
        length_second_half = len(second_half)

        merge_sort(first_half)
        merge_sort(second_half)

        index = 0
        left_index = 0
        right_index = 0

        while left_index < length_first_half and right_index < length_second_half:
            if first_half[left_index] < second_half[right_index]:
                ulist[index] = first_half[left_index]
                left_index += 1
            else:
                ulist[index] = second_half[right_index]
                right_index += 1
            index += 1


        while left_index < length_first_half:
            ulist[index] = first_half[left_index]
            left_index += 1
            index += 1


        while right_index < length_second_half:
            ulist[index] = second_half[right_index]
            right_index += 1
            index += 1


        return ulist
