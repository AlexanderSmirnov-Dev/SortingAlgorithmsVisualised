import random, sys, pygame, time
from pygame.locals import *

pygame.init()

running = True
width = 1200 # window height and widths
height = 800
display = pygame.display.set_mode([width,height])
display.fill(pygame.Color(100,100,100)) # sets background to grey
side_padding = 100
upper_padding = 50

# bar colour choice
colours = ["#B35512","#CB6015","#D96716"]

# running config
list_length = 100
min_val = 0
max_val = 100


# random number generation
def random_list(length,lower_bound,upper_bound):
    """
    generates random list based on parameters input
    :return: [list]
    """
    rand_list = []
    for i in range(length):
        rand_list.append(random.randint(lower_bound,upper_bound))

    return rand_list

def draw_list(given_list):

    allowable_pixels = width - side_padding  # finding individual rectangle width
    pixel_per_rect = round(allowable_pixels / list_length)
    max_height = height - upper_padding
    height_scaling = max_height // max(unsorted_list)

    for i,val in enumerate(given_list):
        colour_num = i % len(colours)
        if colour_num == 0:
            colour_pick = colours[0]
        elif colour_num == 1:
            colour_pick = colours[1]
        else:
            colour_pick = colours[2]
        pygame.draw.rect(display,colour_pick,[(side_padding//2) + pixel_per_rect * i,height-val*height_scaling,pixel_per_rect,val*height_scaling])
        pygame.draw.rect(display,(100,100,100),[(side_padding//2) + pixel_per_rect * i,upper_padding,pixel_per_rect,(height-upper_padding)-val*height_scaling])

def selection_sort(given_list):
    for i,val in enumerate(given_list[0:len(given_list)-1]):
        mini = min(given_list[i:len(given_list)])
        mini_last_index = len(given_list) - 1 - given_list[::-1].index(mini)
        given_list[mini_last_index],given_list[i] = given_list[i],given_list[mini_last_index]
        draw_list(given_list)
        pygame.display.update()
        time.sleep(0.1)

while running: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                unsorted_list = random_list(list_length, min_val, max_val)
                selection_sort(unsorted_list)
    pygame.display.update()



