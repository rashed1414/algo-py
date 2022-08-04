from algo.__init__ import *

def selection_sort(draw_info, ascending=True):
	lst = draw_info.lst
	for i in range(len(lst)):
		idx=i
		for j in range(i+1,len(lst)):
			num1=lst[idx]
			num2=lst[j]
			if (num1>num2 and ascending ) or (num1<num2 and not ascending ):
				idx=j
		lst[i] , lst[idx]=lst[idx], lst[i]
		draw_list(draw_info,{idx:draw_info.Green,idx+1:draw_info.Red},True)
		yield True

	return lst,sound()