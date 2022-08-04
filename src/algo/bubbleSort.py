from algo.__init__ import *

def bubble_sort(draw_info,ascending=True):
    lst=draw_info.lst
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            num1=lst[j]
            num2=lst[j+1]
            if (num1>num2 and ascending) or (num1<num2 and not ascending):
                lst[j],lst[j+1] = lst[j+1],lst[j]
                draw_list(draw_info,{j:draw_info.Green,j+1:draw_info.Red},True)
                yield True
    return lst,sound()