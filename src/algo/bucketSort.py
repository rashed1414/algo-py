from algo.__init__ import *


def insertionSort(b,ascending):
    ##print(asc)
    lst=b
    
    for i in range(1,len(lst)):
        cursor=lst[i]
        while True:
            ascending_sort=i>0 and lst[i-1]> cursor and ascending
            descending_sort=i>0 and lst[i-1]< cursor and not ascending 
            if not descending_sort and not ascending_sort:
                break 
            lst[i]=lst[i-1]
            i=i-1
            lst[i]=cursor
    
    return b      

def bucket_sort(draw_info, ascending=True):
    lst=draw_info.lst
    arr = []
    slot_num = 11
    for i in range(slot_num):
        arr.append([])
    # Put array elements in different buckets
    for j in lst:
        ixd=j*0.01
        index_b = int(10*ixd)
        arr[index_b].append(j)
    # Sort individual buckets
    if not ascending :
        x=[]
        for i in range(-1,-12,-1):
            x.append(insertionSort(arr[i],ascending))
        arr=x
            
    else:       
        for i in range(slot_num):
            arr[i] = insertionSort(arr[i],ascending)
    
    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            lst[k] = arr[i][j]
            k += 1
            draw_list(draw_info,{i:draw_info.Green,j:draw_info.Red},True)
            yield True
    return lst,sound()