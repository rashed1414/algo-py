from algo.__init__ import *


def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst
    if len(lst) > 1:

        # Finding the mid of the array
        mid = len(lst)//2

        # Dividing the array elements
        L = lst[:mid]

        # into 2 halves
        R = lst[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1
        draw_list(draw_info, {j: draw_info.Green, j+1: draw_info.Red}, True)
        yield True

    print(lst)
    return lst
