import random, sys, pygame, time, math
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
list_length = 128
min_val = 0
max_val = 100
sleep_length = 0.01

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
    pygame.display.update()
    time.sleep(sleep_length)

def selection_sort(given_list):
    for i,val in enumerate(given_list[0:len(given_list)-1]):
        mini = min(given_list[i:len(given_list)])
        mini_last_index = len(given_list) - 1 - given_list[::-1].index(mini)
        given_list[mini_last_index],given_list[i] = given_list[i],given_list[mini_last_index]
        draw_list(given_list)

#need to make it work for lists of odd length. Tricky w/ using two pointers
def merge_sort(given_list):  # in place merge sort, non-recursive
    num_iter = round(math.log2(len(given_list))) - 1
    for i in range(num_iter + 1):
        for j in range(0, len(given_list) - 1, 2 ** (i + 1)):
            starter_pointer = j
            middle_pointer = j + 2 ** (i + 1) // 2
            if len(given_list) % 2 == 1 and j == (len(given_list) - 1 - j):
                end = j + 2 ** (i + 1)
            else:
                end = j + 2 ** (i + 1) - 1
            while starter_pointer <= middle_pointer and middle_pointer <= end:
                if given_list[starter_pointer] > given_list[middle_pointer]:
                    shift_val = given_list.pop(middle_pointer)
                    given_list.insert(starter_pointer, shift_val)
                    middle_pointer += 1
                else:
                    starter_pointer += 1
                draw_list(given_list)



while running: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                unsorted_list = random_list(list_length, min_val, max_val)
                merge_sort(unsorted_list)
    pygame.display.update()



