import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from opencv_tutorial.utils import print_array, print_shape, print_plt_image

pic = Image.open('/home/dzas/PycharmProjects/opencv-tutorial/resources/00-puppy.jpg')
pic_arr: np.ndarray = np.asarray(pic)
print_shape(pic_arr)

print_plt_image(pic_arr)

pic_red: np.ndarray = pic_arr.copy()
print_shape(pic_red)
print_array(pic_red)

print_plt_image(pic_arr[:, :, 0])  # show only RED color channel
print_plt_image(pic_arr[:, :, 0], is_gray=True)  # show only RED color channel in a GRAY view

# RGB 0 - 255 # 0 - black 255 - essential color
# Show only RED channel, for that I need to color in black (0) rest of the channels (GREEN and BLUE)
pic_red[:, :, 1] = 0  # color in black GREEN channel
pic_red[:, :, 2] = 0  # color in black BLUE channel

print_plt_image(pic_red)
