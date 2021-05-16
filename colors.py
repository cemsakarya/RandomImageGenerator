import random


def color_generator():
    number_of_colors = 1
    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    return color[0]
