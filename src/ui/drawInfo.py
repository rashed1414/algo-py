import pygame
import math
import random

pygame.init()

class DrawInformation(object):
	
	Black=(0,0,0)
	White=(255,255,255)
	Green=(0,255,0)
	Red=(255,0,0)
	Grey=(128,128,128)
	BACKGROUN_COLOR=White
	GRADIENTS=[(128,128,128),(160,160,160),(192,192,192)]
	
	FONT=pygame.font.SysFont('comicsans',30)

	LARGE_FONT=pygame.font.SysFont('comicsans',45)
	SIDE_PAD=100
	TOP_PAD=120

	def __init__(self, width,height,lst):
        
		self.width = width
		self.height=height

		self.window=pygame.display.set_mode((width,height))
		pygame.display.set_caption("Sorting Visualizer ")

		self.set_list(lst)

	def	set_list(self,lst):
		self.lst=lst
		self.min_val=min(lst)
		self.max_val=max(lst)

		self.block_width=round((self.width-self.SIDE_PAD)/len(lst))
		self.block_height=math.floor((self.height-self.TOP_PAD)/(self.max_val-self.min_val))
		self.start_x=self.SIDE_PAD // 2
  
  
  
def draw(draw_info, algorthm_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUN_COLOR)

    title = draw_info.FONT.render(
    	f"{algorthm_name} | {'Ascending' if ascending else 'Descending'}", 4, draw_info.Black)
    draw_info.window.blit(
    	title, ((draw_info.width/2 - title.get_width()/2), 5))

    controls = draw_info.FONT.render(
    	"R - Reset | SPACE - Start sorting | A - Ascending | D - Descending", 2, draw_info.Black)
    draw_info.window.blit(
    	controls, ((draw_info.width/2 - controls.get_width()/2), 35))

    sorting_algo = draw_info.FONT.render(
    	"I - Insertion Sort | B - Bubble Sort | S - Selection Sort | M - Merge Sort | Q - Quit Sort | K - Bucket Sort | H - Heap Sort", 2, draw_info.Black)
    draw_info.window.blit(
    	sorting_algo, ((draw_info.width/2 - sorting_algo.get_width()/2), 65))

    draw_list(draw_info)
    pygame.display.update()



def draw_list(draw_info, color_position={}, clear_background=False):
    lst = draw_info.lst

    if clear_background:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD//2,
                      draw_info.width - draw_info.SIDE_PAD,
                      draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(
            draw_info.window, draw_info.BACKGROUN_COLOR, clear_rect)
    for i, val in enumerate(lst):
        y = draw_info.height - (val-draw_info.min_val)*draw_info.block_height

        x = draw_info.start_x+i * draw_info.block_width

        color = draw_info.GRADIENTS[i % 3]

        if i in color_position:
            color = color_position[i]

        pygame.draw.rect(draw_info.window, color,
                         (x, y, draw_info.block_width, draw_info.height))
    if clear_background:
        pygame.display.update()



def genarate_starting_list(n_element, min_val, max_val):
	lst = []

	for element in range(n_element):
		val = random.randint(min_val, max_val)
		lst.append(val)

	return lst
