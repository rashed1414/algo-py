from algo.__init__ import *

def insertion_sort(draw_info,ascending=True):
    lst=draw_info.lst
    
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
            draw_list(draw_info,{i-1:draw_info.Green,i:draw_info.Red},True)
            yield True
            

    return lst,sound()