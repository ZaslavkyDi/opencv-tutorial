import numpy as np
import cv2  # import OpenCV

from utils import print_plt_image, print_shape

img: np.ndarray = cv2.imread('/home/dzas/PycharmProjects/opencv-tutorial/resources/00-puppy.jpg')
print(type(img))  # -> numpy.ndarray

# it will show the blue picture because OpenCV and matplotlib expected data in another order channel
# MATPLOTLIB --> RGB
# OPENCV ---> BGR - BLUE GREEN RED
print_plt_image(img)

rgb_fixed_image: np.ndarray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # transform BGR --> RGB
print_plt_image(rgb_fixed_image)

# Show image in gray version
img_gray: np.ndarray = cv2.imread(
    '/home/dzas/PycharmProjects/opencv-tutorial/resources/00-puppy.jpg',
    flags=cv2.IMREAD_GRAYSCALE
)
print_shape(img_gray)
print_plt_image(img_gray, is_gray=True)

# Resizing images
print('Fixed image size')
print_shape(rgb_fixed_image)

# MATPLOTLIB (400, 1000) - (height, width)
# OPENCV (1000, 400) - (width, height)
new_img: np.ndarray = cv2.resize(rgb_fixed_image, (1000, 400))  # OpenCV (1000, 400) - (width, height)
print_shape(new_img)
print_plt_image(new_img)

w_ratio = 0.5  # 50% of the original
h_ration = 0.5

new_img_ration = cv2.resize(  # Resize image with ratio
    rgb_fixed_image,
    dsize=(0, 0),
    dst=rgb_fixed_image,
    fx=w_ratio,
    fy=h_ration
)
print_shape(new_img_ration)
print_plt_image(new_img_ration)

# Flip the image
flipped_image: np.ndarray = cv2.flip(rgb_fixed_image, flipCode=-1)
print_plt_image(flipped_image)

# Save image
cv2.imwrite('test_saved_image.jpg', cv2.cvtColor(flipped_image, cv2.COLOR_RGB2BGR))
