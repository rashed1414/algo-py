from ui.drawInfo import DrawInformation,genarate_starting_list,draw
from algo.bubbleSort import bubble_sort
from algo.insertionSort import insertion_sort
from algo.quickSort import quick_sort
from algo.bucketSort import bucket_sort
from algo.mergeSort import merge_sort
from algo.heapSort import heap_sort
from algo.selectionSort import selection_sort

import pygame 




def main():
	run=True
	clock=pygame.time.Clock()

	n=50
	min_val=0
	max_val=100
	

	lst=genarate_starting_list(n,min_val,max_val)
	draw_info=DrawInformation(1300,600,lst)
	sorting=False
	ascending=True
 
	sorting_algorthm=bubble_sort
	sorting_algorthm_name="Bubble Sort"
	sorting_algorthm_generator=None
	while run:
		clock.tick(20)

		if sorting:
			try:
				next(sorting_algorthm_generator)
			except StopIteration:
				sorting=False
		else:
			draw(draw_info,sorting_algorthm_name,ascending)

		pygame.display.update()

		for event in pygame.event.get():
      
			if event.type == pygame.QUIT:
				raise SystemExit
			if event.type != pygame.KEYDOWN:
				continue

			if event.key == pygame.K_r:
				lst=genarate_starting_list(n,min_val,max_val)
				draw_info.set_list(lst)
			elif event.key == pygame.K_SPACE and sorting==False:
				sorting=True
				sorting_algorthm_generator=sorting_algorthm(draw_info,ascending)
			elif event.key == pygame.K_a and not sorting:
				ascending=True
			elif event.key == pygame.K_d and not sorting:
				ascending=False
			elif event.key == pygame.K_i and not sorting:
				sorting_algorthm=insertion_sort
				sorting_algorthm_name="Insertion Sort"
				
			elif event.key == pygame.K_b and not sorting:
				sorting_algorthm=bubble_sort
				sorting_algorthm_name="Bubble Sort"
			elif event.key == pygame.K_k and not sorting:
				sorting_algorthm=bucket_sort
				sorting_algorthm_name="Bucket Sort"

			elif event.key == pygame.K_m and not sorting:
				sorting_algorthm=merge_sort
				sorting_algorthm_name="Merge Sort"
    
			elif event.key == pygame.K_s and not sorting:
				sorting_algorthm=selection_sort
				sorting_algorthm_name="Selection Sort"

			elif event.key == pygame.K_q and not sorting:
				sorting_algorthm=quick_sort
				sorting_algorthm_name="Quick Sort"
    
			elif event.key == pygame.K_h and not sorting:
				sorting_algorthm=heap_sort
				sorting_algorthm_name="Heap Sort"
    
			elif event.type==pygame.MOUSEBUTTONDOWN:
				print("hi")
    

	pygame.quit()


if __name__=="__main__":
	main()
