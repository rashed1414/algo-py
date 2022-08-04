from algo.__init__ import *

def heapify(arr, size, i,ascending):
    #print (i,"   ",size,"   ",len(arr))
    root = i  # Initialize largest as root
    left = 2 * root + 1     
    right = 2 * root + 2
    

    # See if left child of root exists and is
    # greater than root
    if (left < size and arr[root] < arr[left] and ascending) or (left < size and arr[root] > arr[left] and not ascending): 
        root = left

    # See if right child of root exists and is
    # greater than root
    if (right < size and arr[root] < arr[right] and ascending) or (right < size and arr[root] > arr[right] and not ascending): 
        root = right

    # Change root, if needed
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]  # swap

        # Heapify the root.
        heapify(arr, size, root,ascending)

# The main function to sort an array of given size

def heap_sort(draw_info, ascending=True):
    lst=draw_info.lst
    size = len(lst)

    # Build a maxheap.
    for i in range( size//2 - 1,-1, -1):
        heapify(lst, size, i,ascending)
    # One by one extract elements
    for i in range(size-1, 0, -1):
        lst[i], lst[0]  =  lst[0], lst[i] # swap
        heapify(lst, i, 0,ascending)
        draw_list(draw_info,{i:draw_info.Green,i+1:draw_info.Red},True)
        yield True
    return lst ,sound()